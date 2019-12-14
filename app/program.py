from time import sleep
from app import settings
from app.crawler import PasteCrawler

while True:
    storage_handler = settings.get_storage_handler()
    paste_crawler = PasteCrawler(storage_handler)
    paste_crawler.crawl()
    sleep(60 * 2)
