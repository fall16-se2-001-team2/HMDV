from geopandas import GeoDataFrame
import json
import geojson
import pandas as pd
from shapely.geometry import shape




#names of columns for pandas
columns = ["name", "GEO_ID","coordinates"]
#holds json data to store in DataFrame
data = []
#holds converted geoJson->Polygon
geometry =[]
coords = []

#open the counties json
with open('Counties_TN.json') as TnCounties:
    countyData = json.load(TnCounties)
#for each county in the data
for record in countyData:
    #store the geojson for future use
    coords.append(record["geometry"])
    #create a record for the DataFrame and append it to the data array
    tempRecord=[record["name"],record["GEO_ID"],record["geometry"]]
    data.append(tempRecord)
#now to create the Polygon objects for GeoDataFrame
for poly in coords:
    #Create geojson geometry
    s = json.dumps(poly)
    # Convert to geojson.geometry.Polygon
    g1 = geojson.loads(s)
    # Feed to shape() to convert to shapely.geometry.polygon.Polygon
    # This will invoke its __geo_interface__ (https://gist.github.com/sgillies/2217756)
    g2 = shape(g1)
    #this is now a shapely Polygon object which GeoPandas uses
    geometry.append(g2)



#create a DataFrame for pandas
CountyFrame = pd.DataFrame(data, columns=columns)
#print the head of the DataFrame to see if it works
#print(CountyFrame.head())

#Create GeoDataFrame from DataFrame
countyDataFrame = GeoDataFrame(CountyFrame,crs=None,geometry=geometry)
#store geoDataFrame in pickle file
countyDataFrame.to_pickle("county_GeoPandas")

#print(countyDataFrame)

#read pickled geodataframe
#countyDataFrame=pd.read_pickle("county_GeoPandas")
#print (countyDataFrame.head())




