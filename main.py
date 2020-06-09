import sys
import time
import eBayScraper
import AmazonScraper

initalPrompt = """
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



website = int(input(initalPrompt))


if website == 1:
    page = AmazonScraper.Amazonpage(input("Enter an Amazon URL >> "))
    amazonTask = int(input(AmazonPrompt))
    if amazonTask == 1:
        print(page.getprice())
    elif amazonTask == 2:
        print(page.getname())
    elif amazonTask == 3:
        print(page.getvendor())
    elif amazonTask == 4:
        print(""" 
        {}
        {}
        {}
        """.format(page.getprice(), page.getname(), page.getvendor()))
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
        """.format(page.getPrice, page.getName, page.getVendor, page.getVendorRating))
    





     


