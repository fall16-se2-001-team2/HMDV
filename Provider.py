import Address
class Provider:
    address = Address()
    longCoord = 0.0
    latCoord = 0.0
    ru = 0.0                        #unique radius from provider
    fu = 0.0                        #unique fade [0-1] from provider
    rd = 0.0                        #default radius from resourceType
    regions = []                    #list of pointers to regions impacted by this provider
    population = []                 #list of population constraints

    def _init_ (self):
        address = Address()
        longCoord = 0.0
        latCoord = 0.0
        ru = 0.0  # unique radius from provider
        fu = 0.0  # unique fade [0-1] from provider
        rd = 0.0  #default radius from resourceType
        regions = []                # list of regions impacted by this provider
        population = []             # list of population constraints

    def _init_(self, longCoord, latCoord, radius, fade, defaultRadius, multiplier, regions, population, address):
        self.longCoord = longCoord
        self.latCoord = latCoord
        self.ru = radius
        self.rd = defaultRadius * multiplier         #the provider's default radius is the product of resourceType's radius and the resource's multiplier
        self.fu = fade
        self.regions = regions
        self.population = population
        self.address = address
