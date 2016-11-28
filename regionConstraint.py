#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Jacob Gantt
# Department Name : Computer and Information Sciences
# File Name                :regionConstraint.py
# Purpose                  :Parse eligibility text for counties and cities
#
# Author			        : Team Pandas, github.com/fall16-se2-001-team2/HMDV
#                                   Product Owner: Isaac Styles (styles@etsu.edu
# Create Date	            : Oct 24, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 28, 2016
# Modified By		: Jacob Gantt
#
#-------------------------------------------------------------------------------------------------------------

from collections import namedtuple
import string

ParseResult = namedtuple("ParseResult", "counties cities stringRemains")

countiesList = ["anderson", "bedford", "benton", "bledsoe", "blount", "bradley", "campbell",
    "cannon", "carroll", "carter", "cheatham", "chester", "claiborne", "clay",
    "cocke", "coffee", "crockett", "cumberland", "davidson", "decatur", "deKalb",
    "dickson", "dyer", "fayette", "fentress", "franklin", "gibson", "giles",
    "grainger", "greene", "grundy", "hamblen", "hamilton", "hancock", "hardeman",
    "hardin", "hawkins", "haywood", "henderson", "henry", "hickman", "houston",
    "humphreys", "jackson", "jefferson", "johnson", "knox", "lakev", "lauderdale",
    "lawrence", "lewis", "lincoln", "loudon", "macon", "madison", "marion",
    "marshall", "maury", "mcminn", "mcnairy", "meigs", "monroe", "montgomery",
    "moore", "morgan", "obion", "overton", "perry", "pickett", "polk", "putnam",
    "rhea", "roane", "robertson", "rutherford", "scott", "sequatchie", "sevier",
    "shelby", "smith", "stewart", "sullivan", "sumner", "tipton", "trousdale",
    "unicoi", "union", "van", "buren", "warren", "washington", "wayne", "weakley",
    "white", "williamson", "wilson"]

twoWordCounties         = ["van buren"]
twoWordCountiesSecond   = ["buren"]

citiesList = ["adams","adamsville","alamo","alcoa","alexandria","algood","allardt",
    "altamont","andersonville","apison","ardmore","arlington","ashland city",
    "athens","atoka","atwood","auburntown","baileyton","baneberry","banner hill",
    "bartlett","baxter","bean station","beersheba springs","bell buckle",
    "belle meade","bells","benton","berry hill","bethel springs","bethpage",
    "big sandy","blaine","bloomingdale","blountville","bluff city","bolivar",
    "bon aqua junction","bowman","braden","bradford","bransford","brentwood",
    "brighton","bristol","brownsville","bruceton","bulls gap","burlison","burns",
    "byrdstown","calhoun","camden","carthage","caryville","castalian springs",
    "cedar hill","celina","centertown","centerville","central","chapel hill",
    "charleston","charlotte","chattanooga","chesterfield","church hill",
    "clarkrange","clarksburg","clarksville","cleveland","clifton","clinton",
    "coalfield","coalmont","collegedale","collierville","collinwood",
    "colonial heights","columbia","cookeville","coopertown","copperhill",
    "cornersville","cottage grove","cottontown","covington","cowan","crab orchard",
    "cross plains","crossville","crump","cumberland city","cumberland gap",
    "dandridge","darden","dayton","decatur","decaturville","decherd","dickson",
    "dodson branch","dover","dowelltown","doyle","dresden","ducktown","dunlap",
    "dyer","dyersburg","eagleton village","eagleville","east cleveland",
    "east ridge","eastview","elgin","elizabethton","elkton","englewood",
    "enville","erin","erwin","estill springs","ethridge","etowah","eva",
    "fairfield","fairfield glade","fairgarden","fairmount","fairview",
    "fall branch","falling water","farragut","fayetteville","fincastle","finger",
    "flat top mountain","flintville","forest hills","franklin","friendship",
    "friendsville","gadsden","gainesboro","gallatin","gallaway","garland",
    "gates","gatlinburg","germantown","gibson","gilt edge","gleason",
    "goodlettsville","gordonsville","graball","grand junction","gray","graysville",
    "green hill","greenback","greenbrier","greeneville","greenfield","grimsley",
    "gruetli-laager","guys","halls","harriman","harrison","harrogate",
    "hartsville","helenwood","henderson","hendersonville",
    "henning","henry","hickory valley","hillsboro","hohenwald","hollow rock",
    "hopewell","hornbeak","hornsby","humboldt","hunter","huntingdon","huntland",
    "huntsville","iron city","jacksboro","jackson","jamestown","jasper",
    "jefferson city","jellico","johnson city","jonesborough","kenton","kimball",
    "kingsport","kingston","kingston springs","knoxville","la follette",
    "la grange","la vergne","lafayette","lake city","lake tansi","lakeland",
    "lakesite","lakewood park","lawrenceburg","lebanon","lenoir city","lewisburg",
    "lexington","liberty","linden","livingston","lobelville","lone oak",
    "lookout mountain","loretto","loudon","louisville","luttrell","lyles",
    "lynchburg","lynnville","madisonville","manchester","martin",
    "maryville","mascot","mason","maury city","maynardville","mcewen","mckenzie",
    "mclemoresville","mcminnville","medina","medon","memphis","michie",
    "middle valley","middleton","midtown","milan","milledgeville","millersville",
    "millington","minor hill","mitchellville","monteagle","monterey","mooresburg",
    "morrison","morristown","moscow","mosheim","mount carmel","mount juliet",
    "mount pleasant","mountain city","mowbray mountain","munford","murfreesboro",
    "nashville","new deal","new hope","new johnsonville","new market",
    "new tazewell","new union","newbern","newport","niota","nolensville",
    "normandy","norris","oak grove","oak grove","oak hill","oak ridge",
    "oakdale","oakland","obion","oliver springs","olivet","oneida",
    "ooltewah","orlinda","orme","palmer","paris","park city",
    "parker's crossroads","parrottsville","parsons","pegram","pelham","petersburg",
    "petros","philadelphia","pigeon forge","pikeville","pine crest","piperton",
    "pittman center","plainview","pleasant hill","pleasant view","portland",
    "powells crossroads","pulaski","puryear","ramer","red bank",
    "red boiling springs","riceville","ridgely","ridgeside","ridgetop","ripley",
    "rives","roan mountain","robbins","rockford","rockwood","rogersville",
    "rossville","rural hill","rutherford","rutledge","sale creek","saltillo",
    "samburg","sardis","saulsbury","savannah","scotts hill","selmer","sevierville",
    "sewanee","seymour","shackle island","sharon","shelbyville","signal mountain",
    "silerton","slayden","smithville","smyrna","sneedville","soddy-daisy",
    "somerville","south carthage","south cleveland","south fulton",
    "south pittsburg","sparta","spencer","spring city","spring hill","springfield",
    "spurgeon","st. joseph","stanton","stantonville","summertown","sunbright",
    "surgoinsville","sweetwater","tazewell","telford","tellico plains",
    "tellico village","tennessee ridge","thompson's station","three way",
    "tiptonville","toone","townsend","tracy city","trenton","trezevant","trimble",
    "troy","tullahoma","tusculum","unicoi","union city","unionville","vanleer",
    "viola","vonore","walden","walland","walnut grove","walnut grove",
    "walnut hill","walterhill","wartburg","wartrace","watauga","watertown",
    "waverly","waynesboro","westmoreland","white bluff","white house","white pine",
    "whiteville","whitwell","wildwood","wildwood lake","williston","winchester",
    "winfield","woodbury","woodland mills","wrigley","yorkville"]

class RegionsConstraint:
    @staticmethod
    #parses strings for cities and counties
    #parameters:
    #   eligibility - string of eligibility, eg. "Washington, Hawkins, Van Buren, and Carter county residents ages 18 to 25."
    #returns:
    #   ParseResult.counties        -   list of counties
    #   ParseResult.cities          -   list of cities
    #   ParseResult.stringRemains   -   eligibility string with counties and cities removed
    def RegionConstraint(eligibility):
        eligWords = eligibility.translate(string.maketrans("",""), string.punctuation).lower().split()
        eligWords.append("")
        counties = RegionsConstraint.CountyConstraint(eligWords)
        cities = RegionsConstraint.CityConstraint(eligWords)
        return ParseResult(counties, cities, " ".join(eligWords))

    #looks for substings like "Washington, Sullivan, and Hawkings Counties" or "Greene County"
    #returns all counties from such strings
    #   looking at it, I think this method needs 
    @staticmethod
    def CountyConstraint(eligWords):
        counties = []

        foundStart= False # True means "Washington"
        foundAnd  = False   # True means "Washington and"
        #foundLast = False  # True means "Washington and Sullivan"
        #foundEnd  = False   # True means "Washington and Sullivan Counties" || "Washington County"

        start = -1
        for i in range(len(eligWords)):
            if eligWords[i] in countiesList:
                if not foundStart:
                    start = i
                    foundStart = True
                elif foundAnd:
                    for j in range(start, i+1):   # start through i-1 is rannge of substring except last word ("counties")
                        if j != i-1:            #i-1 is index of "and"
                            RegionsConstraint.appendCounty(counties, eligWords[j])
                            eligWords[j] = ""
                    foundStart= False
                    foundAnd  = False
            elif eligWords[i] == "and" or eligWords[i] == "or":
                if foundStart:
                    foundAnd = True
            elif eligWords[i] == "county":
                if foundStart:
                    RegionsConstraint.appendCounty(counties, eligWords[start])
                    eligWords[start] = ""
                    foundStart= False
                    foundAnd  = False
            else:
                foundStart= False
                foundAnd  = False        
        return counties

    #appends county to list
    #    also checks for multi-word name counties (Van Buren. Stupid county.)
    #    yay
    @staticmethod
    def appendCounty(counties, county):
        if county in twoWordCountiesSecond:
            twoWordCountiesIndex = twoWordCountiesSecond.index(county)
        else:
            twoWordCountiesIndex = -1
        lastRegion = len(counties)-1
        if twoWordCountiesIndex != -1 and counties[lastRegion] == twoWordCounties[twoWordCountiesIndex].split()[0]:
        #if eligWords[index] is part of 2 word county and last region is first part of that county
            counties[lastRegion] = counties[lastRegion] + " " + county
        else:
            counties.append(county)

    @staticmethod
    def CityConstraint(eligWords):
        cities = []
        start = -1
        for i in range(len(eligWords)):
            for j in range(len(citiesList)):
                if eligWords[i] == citiesList[j].split(' ', 1)[0]:
                    if " " not in citiesList[j]:
                        cities.append(citiesList[j])
                        eligWords[i] = ""
                    else:
                        maybeCitySplit = citiesList[j].split()
                        if i + len(maybeCitySplit) <= len(citiesList):
                            match = True
                            for k in range( len(maybeCitySplit) ):
                                if maybeCitySplit[k] !=  eligWords[i+k]:
                                    match = False
                            if match:
                                cities.append(citiesList[j])
                                for k in range( len(maybeCitySplit) ):
                                    eligWords[i+k] = ""
        return cities

inputArray = [
    "Washington, Hawkins, Van Buren, and Carter county residents ages 18 to 25.",
    "Johnson City and Kingsport residents ages 18 to 25.",
    "Residents of the folowing counties: Washington and Greene."]

for line in inputArray:
    regions = RegionsConstraint.RegionConstraint(line)
    print(line)
    if len(regions.counties) != 0:
        print("  -" + str(regions.counties))
    if len(regions.cities) != 0:
        print("  -" + str(regions.cities))
    print("  -" + regions.stringRemains)
