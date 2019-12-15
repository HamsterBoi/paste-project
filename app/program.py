from time import sleep
import settings
from crawler import PasteCrawler

while True:
    print("Stared Crawling...")
    storage_handler = settings.get_storage_handler()
    paste_crawler = PasteCrawler(storage_handler)
    paste_crawler.crawl()
    print("Finished Crawling, Waiting {} seconds".format(settings.CRAWLER_SECONDS_DELAY))
    sleep(settings.CRAWLER_SECONDS_DELAY)
