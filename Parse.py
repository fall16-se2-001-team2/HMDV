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
        providers.append(Provider())
        providers.append(Provider())
        providers.append(Provider())

        return providers
