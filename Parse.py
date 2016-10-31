from Provider import Provider
import time

class Parse:
    defaultRadius = 10.0
    defaultMulti = 1.0
    timestr = ""
    map
    def _init_(self):
        defaultRadius=10.0
        defaultMulti=1.0

        #set the timestamp to identify the output files
        initTimestamp = time.strftime("%H%M%S")
        print ("initialize parser:" + timestr)

    @staticmethod
    def fromDB (dbCursor):#make static
        providers = []
        providers.append(Provider())
        providers.append(Provider())
        providers.append(Provider())

        return providers

    def toOutFile (map):
        import json
        timestr = time.strftime("%Y%m%d-%H%M%S")

        #write the timestamp, research vars, demographics files, to the database for future reference.

        with open(timestr+'.json', 'w') as fp:
            json.dump(self.map.coords, fp)