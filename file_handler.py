import abc
import io

from models.paste import Paste


class PasteStorage(abc.ABC):
    @abc.abstractmethod
    def save_paste(self, paste_model: Paste):
        pass


class FilePasteStorage(PasteStorage):
    def __init__(self, dir_path):
        self._dir_path = dir_path

    def save_paste(self, paste_model):
        with io.open(self._dir_path + r'/{}'.format(paste_model.paste_id), 'w', encoding="utf-8") as file_handler:
            file_handler.write("Author:\n {}\nTitle:\n {}\nContent:\n {}\ndate:\n {}\n".format(paste_model.author,
                                                                                               paste_model.title,
                                                                                               paste_model.content,
                                                                                               paste_model.date))
