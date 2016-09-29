from Provider import Provider
class Parse:
    defaultRadius = 10.0
    defaultMulti = 1.0
    def _init_(self):
        defaultRadius=10.0
        defaultMulti=1.0

    @staticmethod
    def fromDB (dbCursor):#make static
        providers = []
        providers.append(Provider(0.925,1.124, 0, 0, 0, 0, [], []))
        providers.append(Provider(1.133,1.009, 0, 0, 0, 0, [], []))
        providers.append(Provider(1.875,2.005, 0, 0, 0, 0, [], []))

        return providers
    #query google maps api
    @staticmethod
    def addressToCoord ():
        #query addresses from db
        #use google api to translate to coordinates
        #store coordinates in db
        return 0
