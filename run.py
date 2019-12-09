import requests
import lxml.html
from os import listdir
from os.path import isfile, join

from models.paste import Paste
FILES_PATH = "files"
PASTE_BIN_BASE_URL = "https://pastebin.com"

def get_files_names():
    files_names = [f for f in listdir(FILES_PATH) if isfile(join(FILES_PATH, f))]
    return files_names

pastes_objects = []

html = requests.get(PASTE_BIN_BASE_URL, verify=False)
tree = lxml.html.fromstring(html.text)
paste_links = tree.xpath('//div[@id="menu_2"]//a')
files_names = get_files_names()


for paste_link in paste_links:
    paste_href_id = paste_link.attrib.get("href").split('/')[1]
    if paste_href_id not in files_names:
        html = requests.get(PASTE_BIN_BASE_URL + '/' + paste_href_id, verify=False)
        tree = lxml.html.fromstring(html.text)
        title = tree.xpath('//div[@class="paste_box_info"]//h1')[0]
        author = tree.xpath('//div[@class="paste_box_line2"]//a')
        if author:
            author = author[0].text
        else:
            author = ""
        date = tree.xpath('//div[@class="paste_box_line2"]//span')[0].text
        content = requests.get(PASTE_BIN_BASE_URL + '/raw' + '/' + paste_href_id, verify=False).text
        pastes_objects.append(Paste(paste_href_id, author, title, content, date))
    else:
        print("lol")

print(pastes_objects)
for paste_obj in pastes_objects:
    paste_obj.save_to_file(FILES_PATH)

# title_elem = tree.xpath('//title')[0]
# title_elem = tree.cssselect('title')[0]  # equivalent to previous XPath
# print("title tag:", title_elem.tag)
# print("title text:", title_elem.text_content())
# print("title html:", lxml.html.tostring(title_elem))
# print("title tag:", title_elem.tag)
# print("title's parent's tag:", title_elem.getparent().tag)
