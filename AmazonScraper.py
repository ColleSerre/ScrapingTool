from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

class page:
    def __init__(self, url):
        self.url = urlopen(url)
        self.bs = BS(self.url, 'html.parser')
    def getprice(self):
        raw_price = self.bs.find('span', {'class':'a-size-medium a-color-price offer-price a-text-normal'}).get_text()
        for char in raw_price:
            if char.isnumeric() == False:
                raw_price.replace(char, '')
        print('Price: ' + raw_price)
    def getname(self):
        raw_name = self.bs.find('span', {'id' : 'productTitle'}).get_text()
        print('Product name: ' + raw_name.strip())
    
url = input('Copy-past an amazon url: ')
Page = page(url)
welcome=print("""
                ----------------------------------------------------------
                |                                                        |
                |                   Web Scraping API                     |
                |                                                        |
                |   Features:                                            |
                |                                                        |
                |      {1}--get price from Amazon pages                  |
                |      {2}--get product name from Amazon pages           |
                |                                                        |
                |   Features to come:                                    |
                |                                                        |
                |       * Enter a .txt file and get prices for each line |
                |                                                        |
                ----------------------------------------------------------""")

prompt = 0
try:
    prompt = int(input('##'))
except:
    print('Invalid Input')
    while prompt == 0:
        prompt = int(input('##'))

if prompt == 1:
    Page.getprice()
elif prompt == 2:
    Page.getname()