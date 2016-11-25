#-----------------------------------------------------------------------------
# Map class is meant to replace Folium, which translates python objects into javaScript.
# All measurements are in degrees.
#-----------------------------------------------------------------------------
class Map:#(object): #uncomment this to make Map a superclass
    markers = []
    def _init_(self,location):
        self.latlon = location

    def marker(self,location,popup):
        self.markers.append((location,popup))

    def heatDataToLeaflet(self):
        # write coordinates
        strOut = "["

        for i, provider in self.providers:
            i += 1  # increment counter (1-based)
            strOut += repr(provider)  # add the data structure to the string
            if i == len(self.providers):  # if this is the last provider
                break  # dont add a comma after
            strOut += ","  # else add a comma
        strOut += "]"
        return strOut

    def markerToLeaflet(self):
        for provider in self.providers:
            "L.marker([" + provider.latitude + "," + provider.longitude + "]).bindPopup(" + provider + ").addTo(providers);"

    def save(self, dest):
        import codecs
        li = codecs.open(dest, 'w', 'utf-8')
        li.write('[')
