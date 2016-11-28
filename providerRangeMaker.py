#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Jacob Gantt
# Department Name : Computer and Information Sciences
# File Name                :providerRangeMaker.py
# Purpose                  :Takes provider and coordinates and returns number of people in service area
#
# Author			        : Team Pandas, github.com/fall16-se2-001-team2/HMDV
#                                   Product Owner: Isaac Styles (styles@etsu.edu
# Create Date	            : Nov 20, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 28, 2016
# Modified By		: Jacob Gantt
#
#-------------------------------------------------------------------------------------------------------------


import rasterio
from rasterio.tools.mask import mask
from countyHandler import countyHandler
from PIL import Image
import numpy

def addPeopleServed(providers):
    for provider in providers:
        provider.numOfPeople = getPopulationImpacted(
            provider.latitude,
            provider.longitude,
            provider.ru,
            provider.regions, 
            "tempFile")

def getPopulationImpacted(centerX, centerY, radius, counties, saveName):
    makeCounties(counties, saveName)
    cutBox(centerX, centerY, radius, saveName)
    return cutRange(saveName)

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

    with rasterio.open(saveName + ".tif", "w", **out_meta) as dest:
        dest.write(out_image)

def cutBox(centerX, centerY, radius, saveName):
    box = [{'type': 'Polygon', 'coordinates': [[
        (centerX-radius, centerY-radius),
        (centerX+radius, centerY-radius),
        (centerX+radius, centerY+radius),
        (centerX-radius, centerY+radius)
    ]]}]

    # load the raster, mask it by the polygon and crop it
    with rasterio.open(saveName + ".tif") as src:
        out_image, out_transform = mask(src, box, crop=True)
    out_meta = src.meta.copy()


    # save the resulting raster  
    out_meta.update({"driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
    "transform": out_transform})

    with rasterio.open(saveName + ".tif", "w", **out_meta) as dest:
        dest.write(out_image)

def cutRange(saveName):
    im = Image.open(saveName + ".tif")
    #im.show()
    imarray = numpy.array(im)


    print(imarray.size)
    print(imarray.shape)

    total = 0
    for x in range(0, imarray.shape[0]):
        for y in range(0, imarray.shape[1]):
            if imarray[x][y] > 0:
                #print(imarray[x][y])
                total += imarray[x][y]

    return total

    saveFile = Image.fromarray(imarray)









