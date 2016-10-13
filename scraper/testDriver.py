# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:03:14 2016

@author: jarredwininger
"""
from PageScraper import pageScrape
import requests
import re
from bs4 import BeautifulSoup

#pageScrape("http://tn211.mycommunitypt.com/index.php/component/cpx/?task=resource&id=1449855&search_history_id=66165956")
home = "http://tn211.mycommunitypt.com"
url = "http://tn211.mycommunitypt.com/index.php/component/cpx/?task=search.query&amp;view=&amp;page=1&amp;" \
      "search_history_id=66219371&amp;unit_list=0&amp;akaSort=0&amp;query=%20&amp;simple_query="
nextpage="http://tn211.mycommunitypt.com/index.php/component/cpx/?task=search.query&amp;view=&amp;page=2&amp;" \
      "search_history_id=66219371&amp;unit_list=0&amp;akaSort=0&amp;query=%20&amp;simple_query="
#get html from webpage
r = requests.get(url)
#create soup object to manipulate
soup = BeautifulSoup(r.content)
#search for div that contains the page navigation
data = soup.find("div", {"class" : "pagination"}).find_all("a")
loopVal = data[-2].text

#loop through resources and run pagescraper
for i in range(int(loopVal)):
    r = requests.get(nextpage)
    soup = BeautifulSoup(r.content)
    data = soup.find_all(href=re.compile("task=resource.view"))
    for item in data:
        extension = item.get("href")
        pageScrape(home+extension)
    data = soup.find("div", {"class" : "pagination"}).find_all("a")
    nextpage=home+data[-1].get("href")
