import io


class Paste(object):
    def __init__(self, paste_id, author, title, content, date):
        self._paste_id = paste_id
        self._author = author
        self._title = title
        self._content = content
        self._date = date

    def save_to_file(self, path):
        with io.open(path + r'/{}'.format(self._paste_id), 'w', encoding="utf-8") as file_handler:
            file_handler.write("Author:\n {}\nTitle:\n {}\nContent:\n {}\ndate:\n {}\n".format(self._author,
                                                                                               self._title,
                                                                                               self._content,
                                                                                               self._date))

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._author

    @property
    def content(self):
        return self.content

    @property
    def title(self):
        return self._author
