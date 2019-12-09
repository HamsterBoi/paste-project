import abc

from models.paste import Paste


class PasteStorage(abc.ABC):
    @abc.abstractmethod
    def save_paste(self, paste_model: Paste):
        pass


class FilePasteStorage(PasteStorage):
    def __init__(self, dir_path):
        self._dir_path = dir_path

    def save_paste(self, paste_model):
        pass
