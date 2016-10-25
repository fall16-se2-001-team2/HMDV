import string

class RegionGroup:
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


    def __init__(self):
        self.list = []

    def append(self, region):
        if region in self.twoWordCountiesSecond:
            twoWordCountiesIndex = self.twoWordCountiesSecond.index(region)
        else:
            twoWordCountiesIndex = -1
        lastRegion = len(self.list)-1
        if twoWordCountiesIndex != -1 and self.list[lastRegion] == self.twoWordCounties[twoWordCountiesIndex].split()[0]:
        #if region is part of 2 word county and last region is first part of that county
            self.list[lastRegion] = self.list[lastRegion] + " " + region
        else:
            self.list.append(region)

    def PointInterior(self, cooridantes):
        raise NotImplementedException("Stop that. It'll be done when it's done.")

    def PrintRegions(self):
        for region in self.list:
            print(region)

    def Empty(self):
        return len(self.list) == 0

class RegionsConstraint:
    @staticmethod
    def RegionConstraint(eligibility):
        return RegionsConstraint.CountyConstraint(eligibility)

    #looks for substings like "Washington, Sullivan, and Hawkings Counties" or "Greene County"
    #returns al l counties from such strings
    @staticmethod
    def CountyConstraint(eligibility):
        counties = RegionGroup()

        foundStart= False # True means "Washington"
        foundAnd  = False   # True means "Washington and"
        foundLast = False  # True means "Washington and Sullivan"
        foundEnd  = False   # True means "Washington and Sullivan Counties" || "Washington County"

        words = eligibility.translate(string.maketrans("",""), string.punctuation).lower().split()
        words.append("")
        start = -1
        for i in range(len(words)):
            if words[i] in RegionGroup.countiesList:
                if not foundStart:
                    foundStart = True
                    start = i
                elif foundAnd:
                    foundLast = True
            elif words[i] == "and" or words[i] == "or":
                if foundStart:
                    foundAnd = True
            elif words[i] == "county" or words[i] == "counties" or words[i] == "countys":
                if foundStart:
                    if not foundAnd:
                       #print(words[start])
                       counties.append(words[start])
                    else:
                        #print(words[start])
                        for j in range(start, i):   # start through i-1 is rannge of substring except last word ("counties")
                            if j != i-2:            #i-2 is index of "and"
                                counties.append(words[j])                            
            else:
                foundStart= False
                foundAnd  = False
                foundLast = False
                foundEnd  = False
        return counties


inputArray = []
newRecord = True
with open("/home/jacob/python/textToIdea/listOfEligibilities.txt") as f:
    for line in f:
        if(line=="\n"):
            newRecord = True
        if(line[0:6]!="******"and
            line!="Eligibility description\n" and
            line!="Count: ###\n" and
            line!="[Last resoure name with this eligbility]\n" and
            line!="\n" and
            line[0]!="[" and
            line[0:6]!="Count:"
        ):
            if(newRecord):
                inputArray.append(line)
                newRecord = False
            else:
                inputArray[len(inputArray)-1] = inputArray[len(inputArray)-1] + line


for line in inputArray:
    regions = RegionsConstraint.RegionConstraint(line)
    if not regions.Empty():
        regions.PrintRegions()
        print(".")


regions = RegionsConstraint.RegionConstraint("Washington, Hawkins, Van Buren, and Carter county residents ages 18 to 25.")
regions.PrintRegions()

































