from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
import lxml

driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.get("https://twitter.com/search?q=request%20for%20startup&src")
time.sleep(3)
file = open("tweets.csv" , "w" , encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Tweet","Like","Reply","Retweet","Author","Date"])

a=0
while a<3:
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    i=0
    while i<1:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
        i = i+1

    page_source = browser.page_source
    soup = BeautifulSoup(page_source , "lxml")
    tweets = soup.findAll(attrs={"data-testid":"tweet"})
    for x in tweets:
        content = x.find("div" , attrs={"class":"css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}).text
        reply = x.find("div", attrs={"data-testid": "reply"}).text
        retweet = x.find("div", attrs={"data-testid": "retweet"}).text
        like = x.find("div", attrs={"data-testid": "like"}).text
        date = x.find(attrs={"class":"css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0"}).text
        author = x.find("div" , attrs={"class":"css-901oao css-bfa6kz r-1fmj7o5 r-1qd0xha r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-1udh08x r-3s2u2q r-qvutc0"}).text
        if reply == "":
            reply = "0"
        if retweet == "":
            retweet = "0"
        if like == "":
            like = "0"
        writer.writerow([content,like,reply,retweet,author,date])
    a = a +1


