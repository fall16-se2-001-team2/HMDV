#--------------------------------------------------------------------------
#Render takes an array of pixels and modifies them to depict the final coverage output layer.
#--------------------------------------------------------------------------
import numpy as np
import Map
class Render:
    height = 0
    width = 0
    pixelArray = None
    fArray = None
    map = Map()

    def __init__(self, map, height, width):
        self.map = map
        self.height = height
        self.width = width
        pixelArray = np.empty((height, width))
        listArray = np.empty((height,width))
    #STUB method that returns an array filled with 0 or 1 depending if the pixel is outside of a region
    def createRegionMask(self, provider, map, region):
        pass
    #stub method that returns the smallest square array of pixels that contains a provider's region
    def queryAffectedPixels(self, provider, map):
        region = Region()
        return region

#a temporary holder for a square array of a subset of pixels and it's corresponding location in the World.
class Region:
    xCoord = 0 #measured at the upper left corner
    yCoord = 0 #measured at the upper left corner
    npArray = None #holder for the return

    def __init__(self, x, y, size):
        self.xCoord = x
        self.yCoord = y