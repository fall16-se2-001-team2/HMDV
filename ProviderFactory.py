class ProviderFactory:
    countyBuckets = []          #countyBuckets is a flyweight class that contains a list of each provider in each county
    providers = []              #providers is an array of the providers produced so far

    def _init_ (self, countyBuckets):
        self.countyBuckets = countyBuckets

    def newProvider (self, provider, address):
        provider.addAddress(address)    #add the breakaway stuff to provider
        self.providers.append(provider)

    def getProvider (self, index):
        return self.providers[index]

    #toTuple()
    #This takes the class properties and returns them as a tuple(key, float, float, float, float, float)
    #key is the integer index of the corresponding Provider
    def toTuple(self,index):
        return (len(self.providers), self.providers[index].longCoord, self.providers[index].latCoord, self.providers[index].radius, self.providers[index].fade, self.providers[index].defaultRadius*self.providers[index].multiplier)

    #places the provider in the county bucket and an index to the bucket in provider.regions.
    def placeInCountyBucket(self, provider):

        #is the provider in the polygon algorithm.
        # possible solution: divide and conquer solution on county line data
        return 0 #index to particular county in countyBuckets[]