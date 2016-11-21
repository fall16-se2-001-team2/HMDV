import rasterio
from rasterio.tools.mask import mask
from countyHandler import countyHandler
import time

def makeRange(centerX, centerY, radius, counties, saveName):
    makeCounties(counties, saveName)
    cutBox(centerX, centerY, radius, saveName)

def makeCounties(counties, saveName):
    geoms = []
    if type(counties[0]) is str:
        for county in counties:        
            geoms.append(countyHandler.get_county(county).geo)
            geoms.append(countyHandler.get_county(county).geo)
    else:
        for county in counties:        
            geoms.append(county.geo)
            geoms.append(county.geo)

    # load the raster, mask it by the polygon and crop it
    with rasterio.open("/home/jacob/python/SeiiData/gpw-v4-population-density_2015.tif") as src:
        out_image, out_transform = mask(src, geoms, crop=True)
    out_meta = src.meta.copy()


    # save the resulting raster  
    out_meta.update({"driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
    "transform": out_transform})

    with rasterio.open(saveName + ".tiff", "w", **out_meta) as dest:
        dest.write(out_image)

def cutBox(centerX, centerY, radius, saveName):
    box = [{'type': 'Polygon', 'coordinates': [[
        (centerX-radius, centerY-radius),
        (centerX+radius, centerY-radius),
        (centerX+radius, centerY+radius),
        (centerX-radius, centerY+radius)
    ]]}]

    # load the raster, mask it by the polygon and crop it
    with rasterio.open(saveName + ".tiff") as src:
        out_image, out_transform = mask(src, box, crop=True)
    out_meta = src.meta.copy()


    # save the resulting raster  
    out_meta.update({"driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
    "transform": out_transform})

    with rasterio.open(saveName + "2.tiff", "w", **out_meta) as dest:
        dest.write(out_image)
