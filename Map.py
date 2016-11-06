#-----------------------------------------------------------------------------
# Map superclass contains the underlying county regions, the edge boundary of the map.
# All measurements are in degrees. Surface object converts a map into a descrete set of points.
#-----------------------------------------------------------------------------
class Map:#(object): #uncomment this to make Map a superclass
    counties = []   #STUB array for county boundary coordinates
    providers = []#array of Provider classes
    #xCoordinate = 0.0   #longitude at the upper left hand corner
    #yCoordinate = 0.0   #latitude at the upper left hand corner
    #size = 0.0          #edge length of NxN in degrees
    def _init_(self):
        #spheres = [(0.0,0.0,0.0,0.0)]
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
        #xCoord = 1      #calcXoffset(x)
        #yCoord = 1      #calcYoffset(x)
        #radius = 1.1    #calcBoundaryFillRadius(x)
        self.providers.append(provider)

        #check the geocoding when adding a provider to a map

    def toJavaScriptData (self):
        #write coordinates
        strOut = "["

        for i, provider in self.providers:
            i += 1                          #increment counter (1-based)
            strOut += provider.__repr__()   #add the data structure to the string
            if i == self.providers.count(): #if this is the last provider
                break                       #dont add a comma after
            strOut += ","                   #else add a comma
        strOut += "]"