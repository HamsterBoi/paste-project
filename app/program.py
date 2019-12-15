from time import sleep
import settings
from crawler import PasteCrawler

SECONDS_DELAY = 120
while True:
    print("Stared Crawling...")
    storage_handler = settings.get_storage_handler()
    paste_crawler = PasteCrawler(storage_handler)
    paste_crawler.crawl()
    print("Finished Crawling, Waiting {} seconds".format(SECONDS_DELAY))
    sleep(SECONDS_DELAY)
