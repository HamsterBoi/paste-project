import enum
import os
from storage_handler import TinyDBPasteStorage, FilePasteStorage
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
load_dotenv(verbose=True)
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class StorageType(enum.Enum):
    files = 1
    tinydb = 2


STORAGE_TYPE = int(os.environ.get("STORAGE_TYPE", StorageType.tinydb.value))
CRAWLER_SECONDS_DELAY = int(os.environ.get("CRAWLER_SECONDS_DELAY", 120))
FILES_PATH = os.environ.get("FILES_PATH", "files")
LAST_DATE_FILE_NAME = os.environ.get("LAST_DATE_FILE_NAME", "last_date")
PASTE_BIN_ID_BASE_URL = os.environ.get("PASTE_BIN_ID_BASE_URL", "https://pastebin.com")
TINY_DB_JSON_FILE = os.environ.get("TINY_DB_JSON_FILE", "db.json")
PASTE_BIN_BASE_URL = os.environ.get(
    "PASTE_BIN_BASE_URL", "https://pastebin.com/archive"
)


def get_storage_handler():
    if STORAGE_TYPE == StorageType.tinydb.value:
        return TinyDBPasteStorage(TINY_DB_JSON_FILE)

    if STORAGE_TYPE == StorageType.files.value:
        return FilePasteStorage(FILES_PATH, LAST_DATE_FILE_NAME)

    raise Exception("Invalid storage type")
