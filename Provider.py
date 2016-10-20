class Provider:
    #parsed attributes
    name = ""
    address = ""
    address2 = ""                   #necessary???
    city = ""
    state = ""
    zip = ""
    eligibility = ""
    isMobile = False                #boolean identifying if the provider offers mobile service
    #calculated attributes
    longitude = 0.0
    latitude = 0.0
    ru = 0.0                        #unique radius from provider
    fu = 0.0                        #unique fade [0-1] from provider
    rd = 0.0                        #default radius from resourceType
    regions = []                    #list of pointers to regions impacted by this provider
    population = []                 #list of population constraints
    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, float, float, bool)
    # Purpose:initialize a provider with minimal information
    # -------------------------------------------------------------
    def _init_(self, name, address, address2, city, state, zip, eligibility, defaultRadius, multiplier, isMobile):
        self.rd = defaultRadius * multiplier         #the provider's default radius is the product of resourceType's radius and the resource's multiplier
        self.address = address
        self.address2 = address2
        self.name = name
        self.city = city
        self.zip = zip
        self.state = state
        self.eligibility = eligibility
        self.isMobile = isMobile


    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, bool, float, float)
    # Purpose:initialize a provider with a unique radius and fade
    # -------------------------------------------------------------
    def _init_(self, name, address, address2, city, state, zip, eligibility, isMobile, radius, fade):
        self.address = address
        self.address2 = address2
        self.name = name
        self.city = city
        self.zip = zip
        self.state = state
        self.eligibility = eligibility
        self.isMobile = isMobile
        self.ru = radius                # optional parameters unique radius and fade
        self.fu = fade

    # ------------------------------------------------------------
    # toCoordinates(string)
    # Purpose:translate a physical address to longitude and latitude
    # inputs: address:string
    # outputs: tuple(latitude:float, longitude:float)
    # -------------------------------------------------------------
    @staticmethod
    def toCoordinates(address):
        from geopy import geocoders
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode(address)
        return lat, lng