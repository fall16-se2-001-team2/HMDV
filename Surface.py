#--------------------------------------------------------------------------
#Surface maps a discrete set of pixels to a continuous Map object
#--------------------------------------------------------------------------
import math
import numpy as np
class Surface:
    delta = 0.0                                                     #distance to sample the statistical surface
                                                                    #  this needs to be determined by the ratio of the represented geographical region to the pixel resolution
    zValues = [[]]                                                  # height of the map for the set of discrete sample points

    #--------------------------------------------
    #constructor Surface(float, float)
    #inputs: (longitudal width, latitudal height
    #--------------------------------------------
    def __init__(self, mapWidth, mapHeight):
        sampleWidth =  math.ceil(mapWidth / self.delta)             #int of sample points across the x axis
        sampleHeight = mapHeight / self.delta                       #int of sample points across the y axis
        zValues = [[0 for x in range(sampleWidth)] for y in range(sampleHeight)]    #contains the results of the calculation for each pixel
        pass

    #--------------------------------------------
    #discretize()
    #sample the map for each pixel
    #inputs: (longitudal width, latitudal height
    #--------------------------------------------
    def discretize(self):
        for x in range (self.sampleWidth):                           #calculate the height at each descrete point in the array
            for y in range (self.sampleHeight):
                self.zValues[x][y] = self.calcZ(x*self.delta,y*self.delta)   #the height of the map at (long,lat)
        pass