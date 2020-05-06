from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import sys

class page:
    def __init__(self, url):
        self.url = urlopen(url)
        self.bs = BS(self.url, 'html.parser')
    def getprice(self):
        raw_price = self.bs.find('span', {'class':'a-size-medium a-color-price offer-price a-text-normal'}).get_text()
        # add removal of non-digits using regexs
        for char in raw_price:
            if char.isnumeric() == False:
                raw_price.replace(char, '')
        print(raw_price)

welcome=print("""
----------------------------------------------------------
|                                                        |
|                     Web Scraping API                   |
|                                                        |
|   Features:                                            |
|                                                        |
|      * automate prices  getters from amazon web pages  |
|        {1}--get Price from Amazon pages                |
|                                                        |
|   Features to come:                                    |
|                                                        |
|       * Enter a .txt file and get prices for each line |
|                                                        |
----------------------------------------------------------""")
prompt = int(input())

if prompt == 1:
    url = input('Copy-paste an amazon url ')
    Page = page(url)
    Page.getprice()
else:
    print('Invalid input')