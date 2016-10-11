class Provider:
    #parsed attributes
    name = ""
    address = ""
    address2 = ""
    city = ""
    state = ""
    zip = ""
    eligibility = ""
    isMobile = False                #boolean identifying if the provider offers mobile service
    #calculated attributes
    longCoord = 0.0
    latCoord = 0.0
    ru = 0.0                        #unique radius from provider
    fu = 0.0                        #unique fade [0-1] from provider
    rd = 0.0                        #default radius from resourceType
    regions = []                    #list of pointers to regions impacted by this provider
    population = []                 #list of population constraints

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



    def _init_(self, name, address, address2, city, state, zip, eligibility, defaultRadius, multiplier, isMobile,
               radius, fade):
        self.rd = defaultRadius * multiplier  #the provider's default radius is the product of resourceType's radius and the resource's multiplier
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


    @staticmethod
    def toCoordinates(address):
        from geopy import geocoders
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode(address)
        return lat, lng