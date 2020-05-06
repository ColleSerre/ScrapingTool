from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import time

class page:
    def __init__(self, url):
        self.url = urlopen(url)
        self.bs = BS(self.url, 'html.parser')
    def getprice(self):
        try:
            raw_price = self.bs.find('span', {'id':'price_inside_buybox'}).get_text()
        except:
            raw_price = self.bs.find('span', {'class':'a-size-medium a-color-price offer-price a-text-normal'}).get_text()
        print('Price: ' + raw_price.strip())
    def getname(self):
        try:
            raw_name = self.bs.find('span', {'id' : 'productTitle'}).get_text()
        except:
            raw_name = self.bs.find('span', {'class' : 'a-size-extra-large'}).get_text()
        print('Product name: ' + raw_name.strip())
    def getvendor(self):
        try:
            raw_vendor = self.bs.find('a', {'id':'bylineInfo'}).get_text()
        except:
            raw_vendor = self.bs.find('a', {'class':'a-link-normal'}).get_text()
        print('Vendor: ' + raw_vendor)
    
url = input('Paste an Amazon URL: ')
Page = page(url)
welcome="""
                ----------------------------------------------------------
                |                                                        |
                |                   Web Scraping API                     |
                |                                                        |
                |   Features:                                            |
                |                                                        |
                |      {1}--get price from Amazon pages                  |
                |      {2}--get product name from Amazon pages           |
                |      {3}--get vendor name from Amazon pages            |
                |                                                        |
                |   Features to come:                                    |
                |                                                        |
                |       * Enter a .txt file and get prices for each line |
                |                                                        |
                ----------------------------------------------------------"""

def actions():
    print(welcome)
    try:
        prompt = int(input('##'))
    except:
        print('Invalid Input')
        prompt = int(input('##'))
        time.sleep(1)
        actions()
    if prompt == 1:
        Page.getprice()
        time.sleep(1)
        actions()
    elif prompt == 2:
        Page.getname()
        time.sleep(1)
        actions()
    elif prompt == 3:
        Page.getvendor()
        time.sleep(1)
        actions()

if __name__ == "__main__":
    actions()