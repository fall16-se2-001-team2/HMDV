class ProviderFactory:
    countyBuckets = []
    providers = []
    def _init_ (self):
        self.countyBuckets = []
    def newProvider (self, provider):
        self.providers.append(provider)
    def getProvider (self, index):
        return self.providers[index]
