from dateutil import parser
import requests
import arrow
from storage_handler import PasteStorage
import lxml.html
import abc
from models.paste import Paste
from constants import PASTE_BIN_BASE_URL, PASTE_BIN_ID_BASE_URL


class Crawler(abc.ABC):
    def __init__(self, storage_handler: PasteStorage):
        self.storage_handler = storage_handler
        self.last_date = self.storage_handler.get_last_date()

    @abc.abstractmethod
    def crawl(self):
        pass


class PasteCrawler(Crawler):
    def __init__(self, storage_handler: PasteStorage):
        super().__init__(storage_handler)

    def crawl(self):
        max_date = self.last_date
        pastes_objects = []
        html = requests.get(PASTE_BIN_BASE_URL, verify=False)
        tree = lxml.html.fromstring(html.text)
        paste_links = tree.xpath('//div[@id="menu_2"]//a')

        for paste_link in paste_links:
            try:
                paste_href_id = paste_link.attrib.get("href").split('/')[1]
                html = requests.get(PASTE_BIN_ID_BASE_URL + '/' + paste_href_id, verify=False)
                tree = lxml.html.fromstring(html.text)
                title = tree.xpath('//div[@class="paste_box_info"]//h1')[0].text
                author = tree.xpath('//div[@class="paste_box_line2"]//a')
                if author:
                    author = author[0].text
                else:
                    author = ""
                str_date = tree.xpath('//div[@class="paste_box_line2"]//span')[0].attrib.get("title")
                date = parser.parse(str_date)
                content = requests.get(PASTE_BIN_BASE_URL + '/raw' + '/' + paste_href_id, verify=False).text

                if not self.last_date or date > self.last_date:
                    if not max_date or date > max_date:
                        max_date = date
                    pastes_objects.append(Paste(paste_href_id, author, title, content, date))
            except Exception:
                pass

        for paste_obj in pastes_objects:
            self.storage_handler.save_paste(paste_obj)

        self.last_date = max_date
        self.storage_handler.save_last_date(self.last_date)
