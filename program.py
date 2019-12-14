from time import sleep

from constants import TINY_DB_JSON_FILE
from crawler import PasteCrawler
from storage_handler import TinyDBPasteStorage


while True:
    # file_handler = FilePasteStorage(FILES_PATH, LAST_DATE_FILE_NAME)
    file_handler = TinyDBPasteStorage(TINY_DB_JSON_FILE)
    paste_crawler = PasteCrawler(file_handler)
    paste_crawler.crawl()
    sleep(30)
