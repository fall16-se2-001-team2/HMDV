class Provider:
    #parsed attributes
    name = ""
    address = ""
    eligibility = ""
    isMobile = False                #boolean identifying if the provider offers mobile service
    #calculated attributes
    longitude = 0.0
    latitude = 0.0
    h = 100                           #the relative height of the provider; type int(0,100)
    ru = 0.0                        #unique radius. NOTE this is in DEGREES
    #fu = 0.0                        #unique fade (0-1] from provider
    rd = 0.0                        #default radius from resourceType
    services = []
    regions = []                    #list of pointers to regions impacted by this provider
    population = []                 #list of population constraints
    #-----------------------------------
    # Provider(jsonObj)
    # Purpose: initialize from JSON file
    #-----------------------------------
    def _init_(self,jsonObj):
        self.jsonObj = jsonObj
        self.name = jsonObj.get("name")
        self.address = jsonObj.get("address")
        self.eligibility = jsonObj.get("eligibility")
        self.services = jsonObj.get("topLevelServices")

    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, float, float, bool)
    # Purpose: initialize a provider with minimal information
    # -------------------------------------------------------------
    def _init_(self, name, address, eligibility, defaultRadius, multiplier, isMobile=False):
        self.rd = defaultRadius * multiplier         #the provider's default radius is the product of resourceType's radius and the resource's multiplier
        self.address = address
        #self.address2 = address2
        self.name = name
        self.eligibility = eligibility
        self.isMobile = isMobile


    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, bool, float, float)
    # Purpose:initialize a provider with a unique radius and fade
    # -------------------------------------------------------------
    def _init_(self, name, address, eligibility, isMobile, radius, fade):
        self.address = address
        self.name = name
        self.eligibility = eligibility
        self.isMobile = isMobile
        self.ru = radius                # optional parameters unique radius and fade
        self.fu = fade


    # ------------------------------------------------------------
    # repr()
    # Purpose:describe the provider uniquely in JSON notation.
    # -------------------------------------------------------------
    def __repr__(self):
        #sample: {lat: 24.6408, lng:46.7728, count: 3, radius: 1.134 }
        strOut = "{lat: " + self.latitude + ", lng: " + self.longitude + ", count: " + self.height + + ", radius: " + self.ru + "}"
        return strOut

    def __str__(self):
        return self.name