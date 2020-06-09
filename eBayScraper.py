from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import re

class ebayPage:
    def __init__(self, url):
        self.url = urlopen(url)
        self.bs = BS(self.url, 'html.parser')
    def getPrice(self):
        raw_price = self.bs.find('span', {'id':'prcIsum'}).get_text()
        return raw_price
    def getName(self):
        raw_name = self.bs.find('span', {'id':'vi-lkhdr-itmTitl'}).get_text()
        return raw_name
    def getVendor(self):
        raw_vendor = self.bs.find('span', {'class', 'mbg-nw'}).get_text()
        return raw_vendor
    def getVendorRating(self):
        raw_rating = page.bs.find('div', {'id':'si-fb'}).get_text()
        pattern = re.compile('\\d+(?:\\.\\d+)?%')
        mo = pattern.search(raw_rating)
        print(mo.group())

url = input('enter url >> ')
page = ebayPage(url)