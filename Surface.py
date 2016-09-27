class Surface:
    delta = .001 #distance to sample the
    zValues = [[]]  #height of the map at the discrete sample point
#constructor Surface(float, float)
    #inputs:
    def __init__(self, mapWidth, mapHeight):
        sampleWidth =  mapWidth / self.delta #int of sample points across the x axis
        sampleHeight = mapHeight / self.delta #int of sample points across the y axis
        zValues = [[0 for x in range(sampleWidth)] for y in range(sampleHeight)]
        zValues[x][y] = self.calcZ()
