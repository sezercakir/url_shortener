import random, string
from urllib.error import HTTPError
from urllib.request import Request, urlopen


class URL():
    def __init__(self):
        self.short_url_dictionary = {}
        self.json_dict = {}

    def random_generator(self, x: int) -> string:
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.choice(characters) for i in range(x))


    def url_checker(self, url):
        try:
            if url == "":
                return False
            req = Request(url, None, {
                'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            code = urlopen(req).code
            if code < 400:
                return True
            else:
                return False
        except HTTPError:
            return False
    
