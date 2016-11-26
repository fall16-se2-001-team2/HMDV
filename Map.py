#-----------------------------------------------------------------------------
# Map class is meant to replace Folium, which translates python objects into javaScript.
# All measurements are in degrees.
#-----------------------------------------------------------------------------
class Map:  #36.3134,-82.3534 is JC
    providers = []#list of tuples (lat, lon, height, radius, popup)
    def _init_(self):
        pass

    def addProvider(self, lat, lon, height, radius, popup):
        self.providers.append((lat, lon, height, radius, popup))

    def heatDataToFile(self, handle):
        handle.write('var heatData = {max: 100, data: [')
        # write coordinates

        for i, provider in enumerate(self.providers):
            i += 1  # increment counter (1-based)
            handle.write("{lat: " + str(provider[0]) + ", lng: " + str(provider[1]) + ", count: " + str(provider[2]) + ", radius: " + str(provider[3]) + "}")  # add the data structure to the string
            if i == len(self.providers):  # if this is the last provider
                break  # dont add a comma after
            handle.write( ",\n" ) # else add a comma
        handle.write( "]};")

    #--------------------------------------------------
    # markerToFile (handle)
    # purpose: place markers, create popups, and bind popups to markers


    def markersToFile(self, handle):
        for i, provider in enumerate(self.providers):
            i += 1  # increment counter (1-based)
            handle.write("L.marker([" + str(provider[0]) + "," + str(provider[1]) + "]).bindPopup('" + str(provider[4]).replace("'","&#39;") + "').addTo(providers)")
            if i == len(self.providers):  # if this is the last provider
                handle.write(";")
            else:
                handle.write(",\n")  # else add a comma


    def save(self, dest):
        import codecs, time
        timestr = time.strftime("%Y%m%d-%H%M%S")        #set the timestamp to identify the output files

        #self.html.replace("<$></$>",dataPoints)
        #write the timestamp, research vars, demographics files, to the database for future reference.

        with open("output/"+ timestr+ '.js', 'w') as li:    #write out the dataset to javascript file
            self.heatDataToFile(li)
            self.markersToFile(li)

        with open ('leaflet/template.html','r') as html:    #rename the dataset dependency in the template
            with open (dest, 'w') as outhtml:               #and write the file to the temporary location for display
                line = html.read()
                #if "dataPoints.js" in line:
                line = line.replace("dataPoints","output/"+timestr)
                outhtml.write(line)