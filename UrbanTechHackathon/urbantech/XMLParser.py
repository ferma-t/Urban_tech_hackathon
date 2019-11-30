from bs4 import BeautifulSoup

class XMLParser():

    def __init__(self, *args, **kwargs):
        self._bs = BeautifulSoup()
        