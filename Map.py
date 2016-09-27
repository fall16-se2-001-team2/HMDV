# Map superclass
class Map(object):
    counties = []   #STUB array for county boundary coordintes
    spheres = [(0.0,0.0,0.0,0.0)]#array of tuples (x, y, radius, fade)
    def _init_(self):
        spheres = [(0.0,0.0,0.0,0.0)]
        pass
    def populateWithCounties(self, array):
        counties = array    #set the underlying county data in the superclass
        pass


    #STUB METHOD to parse a geoJSON file to data structure
    def addRegion (self, boundaryCoordinates):
        for element in boundaryCoordinates:
            print (element)
        pass
    def addProvider (self, provider):
        xCoord = 1      #calcXoffset(x)
        yCoord = 1      #calcYoffset(x)
        radius = 1.1    #calcBoundaryFillRadius(x)
        self.spheres.append(provider.toTuple())
        pass