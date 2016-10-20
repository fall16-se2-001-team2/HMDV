# -*- coding: utf-8 -*-
#   Jarred Wininger
#   09/16/2016
#   Page Scraping method for TN211 website


import requests
import json
import os
from bs4 import BeautifulSoup


def pageScrape( url):
    #variable Declaration
    intakeProcedure = ""
    resourceAddress = ""
    resourceDescription = ""
    resourceEligibility = ""
    resourceHours = ""
    resourceName = ""
    resourcePhone = ""
    resourceWebsite = ""
    resourceLanguages = ""
    resourceAccessibility = ""
    serviceList =[]
    
    #home url for webpage
    home = "http://tn211.mycommunitypt.com"
    #get html from webpage
    r = requests.get(url)
    #create soup object to manipulate
    soup = BeautifulSoup(r.content)
    
    #find normal url for page (does not include search id)
    try:
        data = soup.find_all("a")
        for item in data:
            if "tab=1" in item.get("href"): 
                url = home+item.get("href")
                
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
    except:
        print("URL Not Found")
            
    
    #find the resource name and store it
    try:
        data = soup.find_all("p", { "id" : "view_field_name_top"} )
    	
        for item in data:
            resourceName=item.text
    except:
        resourceName = "Not Found"
    finally:
        if not resourceName:
            resourceName = "Not Found"
    
    #find and store resource address
    try:
        data = soup.find_all("p", { "id" : "view_field_primaryAddressId"})
        
        for item in data:
            resourceAddress = item.text
    except:
        resourceAddress = "Not Found"
    finally:
        if not resourceAddress:
            resourceAddress = "Not Found"
    
    #find resources' primary phone number 
    try:  
        data = soup.find_all("p", { "id" : "view_field_primaryTelephone"})
    
        for item in data:
            resourcePhone = item.text
    except:
        resourcePhone = "Not Found"
    finally:
        if not resourcePhone:
            resourcePhone = "Not Found"
     
    #find and store resource's website  
    try: 
        data = soup.find_all("p", { "id" : "view_field_url"})
    
        for item in data:
            resourceWebsite = item.text
    except:
        resourceWebsite = "Not Found"
    finally:
        if not resourceWebsite:
            resourceWebsite = "Not Found"
        
    #find and store Resource Description
    try:
        data = soup.find_all("p", { "id" : "view_field_description"})
    
        for item in data:
            resourceDescription = item.text
    except:
        resourceDescription = "Not Found" 
    finally:
        if not resourceDescription:
            resourceDescription = "Not Found"
        
    #find and store Resource Services
    try:
        data = soup.find_all("a", { "title" : "Toggle Service Details"})
    
        for item in data:
            serviceList.append(item.text)
    except:
        serviceList.appened("Not Found")
    finally:
        if not serviceList:
            serviceList.append("Not Found")
        
    #find and store business hours
    try:
        data = soup.find_all("p", { "id" : "view_field_hours"})
    
        for item in data:
            resourceHours = item.text
    except:
        resourceHours = "Not Found"
    finally:
        if not resourceHours:
            resourceHours = "Not Found"    
        
    #find and store intake process
    try:
        data = soup.find_all("p", { "id" : "view_field_intakeProcedure"})
    
        for item in data:
            intakeProcedure = item.text 
    except:
            intakeProcedure = "Not Found"
    finally:
        if not intakeProcedure:
            intakeProcedure = "Not Found"
            
    #find and store Languages
    try:
        data = soup.find_all("p", { "id" : "view_field_languages"})
    
        for item in data:
            resourceLanguages = item.text
    except:
            resourceLanguages = "Not Found"
    finally:
        if not resourceLanguages:
            resourceLanguages = "Not Found"
            
    #find and store eligibility
    try:
        data = soup.find_all("p", { "id" : "view_field_eligibility"})
    
        for item in data:
            resourceEligibility = item.text
    except:
        resourceEligibility = "Not Found"
    finally:
        if not resourceEligibility:
            resourceEligibility = "Not Found"
        
    #find accessibility to facility
    try:
        data = soup.find_all("p", { "id" : "view_field_accessibility"})
    
        for item in data:
            resourceAccessibility = item.text
    except:
        resourceAccessibility = "Not Found"
    finally:
        if not resourceAccessibility:
            resourceAccessibility = "Not Found"
        
    #is the resource a shelter?
    try:    
        data = soup.find_all("p", { "id" : "view_field_is_shelter"})
        
        for item in data:
                isShelter = item.text
    except:
        isShelter = "Not Found"
    finally:
        if not isShelter:
           isShelter = "Not Found"
    
    #append any secondary resources listed on the details page
    #navigate to details page by replacing the last url character with 2
    #url = url[:-1]
    #url = ''.join(url,'2')
    #url = url + '2'
    
    #r = requests.get(url)
   # soup = BeautifulSoup(r.content, "lxml")
    
    #find and store Resource Services
   # try:
    #    data = soup.find_all("li", { "id" : "view_field_secondaryServices"})
    #    for item in data:
    #        newData = item.find_all("a", {"title" : "Toggle Service Details"})
    #        for newItem in newData:
    #            serviceList.append()
    #    print("HELLO")
        
   # except:
     #   print('No Secondary Services')
    
           
           
    #write to dictionary    
    resourceData = {
        'name' : resourceName,
        'address' : resourceAddress,
        'phone' : resourcePhone,
        'website' : resourceWebsite,
        'description' : resourceDescription,
        'eligibility' : resourceEligibility,
        'intakeProcess' : intakeProcedure,
        'hours' : resourceHours,
        'languages' : resourceLanguages,
        'services' : serviceList,
        'accessibility' : resourceAccessibility,
        'shelter' : isShelter}
    
    #append to json file  
    #to use, change the first open parameter with location of JSON
    with open('C:/Users/Matthew/resource.json', 'a') as f:
        json.dump(resourceData, f)
        f.write(os.linesep)
    
    
    
    
    
    
        
    
    
    
    
    



