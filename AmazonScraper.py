from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import requests


class Amazonpage:
    def __init__(self, url):
        self.url = urlopen(url)
        self.bs = BS(self.url, 'html.parser')
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
                        print('Unexpected Error')
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
    def searchamazon(self, argument):
        argument = argument.replace(" ", "+")
        self.url = urlopen("https://www.amazon.com/s?k=" + argument + "&crid=3IP1LTDR2K41D&sprefix=harry+p%2Caps%2C223&ref=nb_sb_ss_i_1_7")
        self.bs = BS(self.url, 'html.parser')
        
    