from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import sys
import time

class page:
    def __init__(self, url):
        self.url = urlopen(url)
        self.bs = BS(self.url, 'html.parser')
    def readFile(self): # Iterate through each line
        File = open(self.path, 'rt')
        for line in File:
            self.url = line
            if prompt == 1:
                print(self.getprice())
            elif prompt == 2:
                print(self.getname())
            elif prompt == 3:
                print(self.getvendor())



    def getprice(self): ## NOT ELEGANT
        try:
            raw_price = self.bs.find('span', {'id':'price_inside_buybox'}).get_text()
        except:
            try:
                raw_price = self.bs.find('span', {'id':'priceblock_ourprice'}).get_text()
            except:
                try:
                    raw_price = self.bs.find('span', {'class':'a-size-medium a-color-price priceBlockBuyingPriceString'}).get_text()    
                except:
                    try:
                        raw_price = self.bs.find('span', {'class':'a-size-medium a-color-price offer-price a-text-normal'}).get_text()
                    except:
                        print('fatal error')
        return "Price: " + raw_price.strip()
    def getname(self):
        try:
            raw_name = self.bs.find('span', {'id' : 'productTitle'}).get_text()
        except:
            raw_name = self.bs.find('span', {'class' : 'a-size-extra-large'}).get_text()
        return "Product name: " + raw_name.strip()
    def getvendor(self):
        try:
            raw_vendor = self.bs.find('a', {'id':'bylineInfo'}).get_text()
        except:
            try:
                raw_vendor = self.bs.find('a', {'class':'a-link-normal'}).get_text()
            except:
                raw_vendor = self.bs.find('a', {'class':'a-link-normal contributorNameID'}).get_text() # get author doesn't work
        return "Vendor: " + raw_vendor
   
    
url = input('Paste an Amazon URL: ') # add the sys module and a -c flag to get the config file
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
                |      {4}--EXECUTE ALL                                  |
                |                                                        |
                |   Features to come:                                    |
                |                                                        |
                |       * Enter a .txt file and get prices for each line |
                |                                                        |
                ----------------------------------------------------------"""

prompt=0

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
        print(Page.getprice())
        time.sleep(1)
        actions()
    elif prompt == 2:
        print(Page.getname())
        time.sleep(1)
        actions()
    elif prompt == 3:
        print(Page.getvendor())
        time.sleep(1)
        actions()
    elif prompt == 4:
        print("""Product information:
                    -""" + str(Page.getname())+"""
                    -""" + str(Page.getprice())+"""
                    -""" + str(Page.getvendor()))

if __name__ == "__main__":
    actions()

#To do:
#   * Add for each line do method feature