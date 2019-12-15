from time import sleep
import settings
from crawler import PasteCrawler

from app.settings import CRAWLER_SECONDS_DELAY

while True:
    print("Stared Crawling...")
    storage_handler = settings.get_storage_handler()
    paste_crawler = PasteCrawler(storage_handler)
    paste_crawler.crawl()
    print("Finished Crawling, Waiting {} seconds".format(CRAWLER_SECONDS_DELAY))
    sleep(CRAWLER_SECONDS_DELAY)
