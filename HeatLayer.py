from Provider import Provider

class HeatLayer:
    defaultRadius = 1.0
    defaultMulti = 1.0
    
    def _init_(self,templateFile):
        pass


    def toOutFile (self, dataPoints, countyJSONAddr):
        import codecs, json, time
        f = codecs.open(countyJSONAddr, 'r', 'utf-8')
        resourceList = json.load(f)
        f.close()
        timestr = time.strftime("%Y%m%d-%H%M%S")        #set the timestamp to identify the output files

        #self.html.replace("<$></$>",dataPoints)
        #write the timestamp, research vars, demographics files, to the database for future reference.

        outFile = open(timestr+".js", "w")            #write the html file with dataPoints
        outFile.write(self.js)
        outFile.close()
        #with open(timestr+'.json', 'w') as fp:
        #    json.dump(self.map.coords, fp)