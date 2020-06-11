import sys
import time
import eBayScraper
import AmazonScraper



def countDown(n):
    while True:
        if n >= 0:
            print("Wait " + str(n) + " seconds before making an new request")
            n -= 1
            time.sleep(1)
        else:
            break
        



initialPrompt = """
Which website do you want to scrape?
    {1} - Amazon
    {2} - eBay
>> """

AmazonPrompt = """
 -----------------------------
|      Amazon WebScraper      |      
|                             |
|    {1} - Get price          |   
|    {2} - Get product name   |
|    {3} - Get vendor name    |
|    {4} - Get all            |
|    {5} - Search Amazon      |
 -----------------------------
"""
ebayPrompt = """
 -----------------------------
|      eBay WebScraper        |      
|                             |
|    {1} - Get price          |   
|    {2} - Get product name   |
|    {3} - Get vendor name    |
|    {4} - Get vendor grade   |
|    {5} - Get all            |
 -----------------------------
"""




while True:

    website = int(input(initialPrompt))

    if website == 1:
        amazonTask = int(input(AmazonPrompt))
        if amazonTask == 1:
            page = AmazonScraper.Amazonpage(input("Enter an Amazon URL >> "))
            print(page.getprice())
        elif amazonTask == 2:
            page = AmazonScraper.Amazonpage(input("Enter an Amazon URL >> "))
            print(page.getname())
        elif amazonTask == 3:
            page = AmazonScraper.Amazonpage(input("Enter an Amazon URL >> "))
            print(page.getvendor())
        elif amazonTask == 4:
            page = AmazonScraper.Amazonpage(input("Enter an Amazon URL >> "))
            print(""" 
            {}
            {}
            {}
            """.format(page.getprice(), page.getname(), page.getvendor()))
        elif amazonTask == 5:
            page = AmazonScraper.Amazonpage("https://google.com")
            argument = input("Enter keywords >> ")
            argument = argument.replace(" ", "+")
            url = "https://www.amazon.com/s?k="+argument+"&ref=nb_sb_noss_2"
            headers = {'user agent':"Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"}
            r = AmazonScraper.requests.get(url, headers=headers)
            page.bs = AmazonScraper.BS(r.text, 'html.parser')
            print(page.bs)

    elif website == 2:
        page = eBayScraper.ebayPage(input("Enter an eBay URL >> ")) 
        ebayTask = int(input(ebayPrompt))
        if ebayTask == 1:
            print(page.getPrice())
        elif ebayTask == 2:
            print(page.getName())
        elif ebayTask == 3:
            print(page.getVendor())
        elif ebayTask == 4:
            print(page.getVendorRating())
        elif ebayTask == 5:
            print(""" 
            {}
            {}
            {}
            {}        
            """.format(page.getPrice(), page.getName(), page.getVendor(), page.getVendorRating()))
    countDown(10)
    



    





     


