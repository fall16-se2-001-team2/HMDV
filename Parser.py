class Parser:
    #--------------------------------------------------------------------
    # parseCounties - static
    # Purpose: convert a typical geoJSON into one accepted by leaflet,
    #          and encapsulate it in a javaScript file.
    #--------------------------------------------------------------------
    @staticmethod
    def parseCounties(countyJSONSource="data/counties_TN.json", dest="leaflet/counties_TN.js"):
        js = "var countyData = {\"type\":\"FeatureCollection\",\"features\":["
        import codecs, json
        with open(countyJSONSource) as f:
            countiesData = json.load(f)
        count = 0
        for c in countiesData:

            js += "{\"type\":\"Feature\",\"properties\":{\"name\":\""
            js += c["name"] + "\"},\"geometry\": {\"type\": \""
            js += c["geometry"]["type"] + "\",\"coordinates\":["
            geometries = c["geometry"]["coordinates"]
            gCount = 0
            for geometry in geometries:
                js += "["
                cCount = 0
                for coord in geometry:
                    js += "[" + str(coord[0]) + "," + str(coord[1]) + "]"
                    cCount += 1
                    if cCount == len(geometry):
                        js += "]"  # close this particular geometry
                        break
                    js += ","
                gCount += 1
                if gCount == len(geometries):
                    js += "]"
                    break
                js += ","
            js += "}}"
            count += 1
            if len(countiesData) == count:
                break
            js += ","
        js += "]}"
        li = codecs.open(dest, 'w', 'utf-8')
        li.write(js)
        li.close()