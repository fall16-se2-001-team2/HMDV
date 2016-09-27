class Provider:
    coordinates = (0.0,0.0)         #longitude and latitude
    ru = 0.0                        #unique radius from provider
    fu = 0.0                        #unique fade [0-1] from provider
    rd = 0.0                        #default radius from resourceType
    regions = []                    #list of regions impacted by this provider
    population = []                 #list of population constraints

    def _init_ (self):
        coordinates = (0.0, 0.0)    # longitude and latitude
        ru = 0.0                    # unique radius from provider
        fu = 0.0                    # unique fade [0-1] from provider
        rd = 0.0                    # default radius from resourceType
        regions = []                # list of regions impacted by this provider
        population = []             # list of population constraints

    def _init_(self, coordinates, radius, fade, defaultRadius, multiplier, regions, population):
        coordinates = coordinates
        ru = radius
        rd = defaultRadius * multiplier         #the provider's default radius is the product of resourceType's radius and the resource's multiplier
        fu = fade
        regions = regions
        population = population

    #toTuple()
    #This takes the class properties and returns them as a tuple(float, float, float, float, float)
    def toTuple(self):
        return (self.coordinates(0),self.coordinates(1),self.ru,self.rf,self.rd)
