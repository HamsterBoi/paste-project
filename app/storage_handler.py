import abc
import io
from tinydb import TinyDB, Query
from dateutil import parser
from models.paste import Paste
import os.path


class PasteStorage(abc.ABC):

    @abc.abstractmethod
    def save_paste(self, paste_model: Paste):
        pass

    @abc.abstractmethod
    def get_last_date(self):
        pass

    @abc.abstractmethod
    def save_last_date(self, date):
        pass


class TinyDBPasteStorage(PasteStorage):
    def __init__(self, db_file):
        if not os.path.isfile(db_file):
            with io.open(db_file, 'w', encoding="utf-8") as file_handler:
                file_handler.write("")

        self.db = TinyDB(db_file)

    def save_paste(self, paste_model: Paste):
        self.db.insert({
            "author": paste_model.author,
            "title": paste_model.title,
            "content": paste_model.content,
            "date": str(paste_model.date)
        })

    def get_last_date(self):
        db_query = Query()
        query_result = self.db.search(db_query.type == "config")
        if query_result:
            return parser.parse(query_result[0].get("last_date"))

    def save_last_date(self, date):
        db_query = Query()
        self.db.upsert({'last_date': str(date), "type": "config"}, db_query.type == "config")


class FilePasteStorage(PasteStorage):
    def __init__(self, dir_path, last_date_file_name):
        self._dir_path = dir_path
        self._last_date_file_name = last_date_file_name

    def save_paste(self, paste_model):
        with io.open(self._dir_path + r'/{}'.format(paste_model.paste_id), 'w', encoding="utf-8") as file_handler:
            file_handler.write("Author:\n {}\nTitle:\n {}\nContent:\n {}\ndate:\n {}\n".format(paste_model.author,
                                                                                               paste_model.title,
                                                                                               paste_model.content,
                                                                                               paste_model.date))

    def save_last_date(self, date):
        with io.open("{}/{}".format(self._dir_path, self._last_date_file_name), 'w', encoding="utf-8") as file_handler:
            file_handler.write(str(date))

    def get_last_date(self):
        try:
            with io.open("{}/{}".format(self._dir_path, self._last_date_file_name), 'r',
                         encoding="utf-8") as file_handler:
                str_date = file_handler.read()
        except Exception:
            return None

        return parser.parse(str_date)
