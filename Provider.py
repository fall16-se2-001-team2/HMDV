class Provider:
    #parsed attributes
    name = ""
    address = ""
    eligibility = ""
    desc = ""
    phone = ""
    isShelter = False                #boolean identifying if the provider offers shelter
    #calculated attributes
    longitude = None
    latitude = None
    h = 100                           #the relative height of the provider; type int(0,100)
    ru = 0.0                        #unique radius. NOTE this is in DEGREES
    #fu = 0.0                        #unique fade (0-1] from provider
    rd = 0.0                        #default radius from resourceType
    services = []
    topLevelServices = []
    isMobile = False                #boolean identifying if the provider offers mobile service
    jsonObj = None                  #data structure so the program can output the complete resource file
    #regions = []                    #list of pointers to regions impacted by this provider
    #population = []                 #list of population constraints
    #-----------------------------------
    # Provider(jsonObj)
    # Purpose: initialize from JSON file
    #-----------------------------------
    def __init__(self,jsonObj):
        self.jsonObj = jsonObj
        self.name = jsonObj["name"]
        self.address = jsonObj["address"]
        self.eligibility = jsonObj["eligibility"]
        self.services = jsonObj["services"]
        self.desc = jsonObj["description"]
        self.phone = jsonObj["phone"]
        if "topLevelServices" in jsonObj:
            self.topLevelServices = jsonObj["topLevelServices"]
        if "longitude" in jsonObj:      #check to see if previously geocoded
            self.longitude = jsonObj["longitude"]
            self.latitude = jsonObj["latitude"]
        if "ru" in jsonObj:
            self.ru = float(jsonObj["ru"])
    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, float, float, bool)
    # Purpose: initialize a provider with minimal information
    # -------------------------------------------------------------
    """def __init__(self, name, address, eligibility, defaultRadius, multiplier, isMobile=False):
        self.rd = defaultRadius * multiplier         #the provider's default radius is the product of resourceType's radius and the resource's multiplier
        self.address = address
        #self.address2 = address2
        self.name = name
        self.eligibility = eligibility
        self.isMobile = isMobile"""
    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, bool, float, float)
    # Purpose:initialize a provider with a unique radius and fade
    # -------------------------------------------------------------
    """def __init__(self, name, address, eligibility, isMobile, radius, fade):
        self.address = address
        self.name = name
        self.eligibility = eligibility
        self.isMobile = isMobile
        self.ru = radius                # optional parameters unique radius and fade
        self.fu = fade"""
    def setLatLon (self, lat, lon):
        self.latitude = lat
        self.longitude = lon
    # ------------------------------------------------------------
    # repr()
    # Purpose:describe the provider uniquely in JSON notation.
    # -------------------------------------------------------------

    def __str__(self):
        return self.name