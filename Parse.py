from Provider import Provider
import time

class Parse:
    defaultRadius = 10.0
    defaultMulti = 1.0
    html = ""
    def _init_(self,templateFile):
        defaultRadius=10.0
        defaultMulti=1.0
        f = open(templateFile, 'r') #open the leaflet template
        html = f.read()
        f.close()



    def toOutFile (self,dataPoints):
        import json
        timestr = time.strftime("%Y%m%d-%H%M%S")        #set the timestamp to identify the output files

        self.html.replace("<$></$>",dataPoints)
        #write the timestamp, research vars, demographics files, to the database for future reference.

        outFile = open(timestr+".html", "w")            #write the html file with dataPoints
        outFile.write(self.html)
        outFile.close()
        #with open(timestr+'.json', 'w') as fp:
        #    json.dump(self.map.coords, fp)