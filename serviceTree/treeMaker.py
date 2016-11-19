# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:03:14 2016

@author: jarredwininger
"""
import requests
import re
import json
from bs4 import BeautifulSoup

#pageScrape("http://tn211.mycommunitypt.com/index.php/component/cpx/?task=resource&id=1449855&search_history_id=66165956")
home = "http://tn211.mycommunitypt.com"
url = "http://tn211.mycommunitypt.com/index.php/component/cpx/?task=services.tree"
basicpage="http://tn211.mycommunitypt.com/index.php/component/cpx/?task=services.tree&code=Y"
lastpage="http://tn211.mycommunitypt.com/index.php/component/cpx/?task=services.tree&code=TR-8000.8000-950"
#get html from webpage
r = requests.get(url)
#create soup object to manipulate
soup = BeautifulSoup(r.content,"html.parser")
#search for div that contains the page navigation
toplevel = soup.find_all("h3")
codes = {}
jdump = {}

for link in toplevel:
    name = link.__str__()
    name = str.split(name,">",10)[2]
    name = str.split(name,"<",2)[0]
    code = link.__str__()
    code = str.split(code,"code=",10)[1]
    code = str.split(code,"\"",2)[0]
    codes[code] = name

for c,n in sorted(codes.items()):
    r1 = requests.get(basicpage+c)
    # create soup object to manipulate
    soup1 = BeautifulSoup(r1.content,"html.parser")
    # search for div that contains the page navigation
    level1 = soup1.find_all("h3")
    codes1 = {}
    jdump["name"] = n
    jdump["topLevelName"] = n
    with open('C:\\Users\\Matthew\\PycharmProjects\\HMDV\\data\\servicetree.json', 'a') as f:
        json.dump(jdump, f)
        f.close()
    jdump.clear()
    if(c != "B" or c != "D" or c != "F" or c != "H" or c != "J"):

        for link in level1:
            name1 = link.__str__()
            name1 = str.split(name1, ">", 10)[2]
            name1 = str.split(name1, "<", 2)[0]
            code1 = link.__str__()
            code1 = str.split(code1, "code=", 10)[1]
            code1 = str.split(code1, "\"", 2)[0]
            codes1[code1] = name1
            jdump["name"] = name1
            jdump["topLevelName"] = n
            with open('C:\\Users\\Matthew\\PycharmProjects\\HMDV\\data\\servicetree.json', 'a') as f:
                json.dump(jdump, f)
                f.close()
            jdump.clear()

        for c2, n2 in sorted(codes1.items()):
            r2 = requests.get(basicpage + c2)
            # create soup object to manipulate
            soup2 = BeautifulSoup(r2.content, "html.parser")
            # search for div that contains the page navigation
            level2 = soup2.find_all("h3")
            codes2 = {}

            for link2 in level2:
                name2 = link2.__str__()
                name2 = str.split(name2, ">", 10)[2]
                name2 = str.split(name2, "<", 2)[0]
                code2 = link2.__str__()
                code2 = str.split(code2, "code=", 10)[1]
                code2 = str.split(code2, "\"", 2)[0]
                codes2[code2] = name2

            for c3, n3 in sorted(codes2.items()):
                r3 = requests.get(basicpage + c3)
                # create soup object to manipulate
                soup3 = BeautifulSoup(r3.content, "html.parser")
                # search for div that contains the page navigation
                level3 = soup3.find_all("h3")
                codes3 = {}

                for link3 in level3:
                    name3 = link3.__str__()
                    name3 = str.split(name3, ">", 10)[2]
                    name3 = str.split(name3, "<", 2)[0]
                    code3 = link3.__str__()
                    code3 = str.split(code3, "code=", 10)[1]
                    code3 = str.split(code3, "\"", 2)[0]
                    codes3[code3] = name3

                for c4, n4 in sorted(codes3.items()):
                    r4 = requests.get(basicpage + c4)
                    # create soup object to manipulate
                    soup4 = BeautifulSoup(r4.content, "html.parser")
                    # search for div that contains the page navigation
                    level4 = soup4.find_all("h3")
                    codes4 = {}

                    for link4 in level4:
                        name4 = link4.__str__()
                        name4 = str.split(name4, ">", 10)[2]
                        name4 = str.split(name4, "<", 2)[0]
                        code4 = link4.__str__()
                        code4 = str.split(code4, "code=", 10)[1]
                        code4 = str.split(code4, "\"", 2)[0]
                        codes4[code4] = name4

                        for c5, n5 in sorted(codes4.items()):
                            r5 = requests.get(basicpage + c5)
                            # create soup object to manipulate
                            soup5 = BeautifulSoup(r5.content, "html.parser")
                            # search for div that contains the page navigation
                            level5 = soup4.find_all("h3")
                            codes5 = {}

                            for link5 in level5:
                                name5 = link5.__str__()
                                name5 = str.split(name5, ">", 10)[2]
                                name5 = str.split(name5, "<", 2)[0]
                                jdump["name"] = name5
                                jdump["topLevelName"] = n
                                jdump["secondLevelName"] = n2
                                jdump["thirdLevelName"] = n3
                                with open('C:\\Users\\Matthew\\PycharmProjects\\HMDV\\data\\servicetree.json', 'a') as f:
                                    json.dump(jdump, f)
                                    f.close()
                                jdump.clear()