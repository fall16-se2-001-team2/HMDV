#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Jacob Gantt
# Department Name : Computer and Information Sciences
# File Name                :test_driver.py
# Purpose                  :Tests functionality of countyHandler and providerRangeMaker
#
# Author			        : Team Pandas, github.com/fall16-se2-001-team2/HMDV
#                                   Product Owner: Isaac Styles (styles@etsu.edu
# Create Date	            : Nov 14, 2016
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
from providerRangeMaker import getPopulationImpacted
from ProviderList import ProviderList

print("start")
print(countyHandler.get_county("cocke").nameFull)
print(countyHandler.get_county("washington").nameFull)
print(countyHandler.get_county("van buren").nameFull)

counties = []
counties.append(countyHandler.get_county("sullivan"))
counties.append(countyHandler.get_county("washington"))
counties.append(countyHandler.get_county("unicoi"))

total = getPopulationImpacted(-82.4725, 36.294167, 0.2, counties, "save")

print(total)

providersList = ProviderList('data/resourceLatLon.json',topLevels[0], 25, 1000)

print( providersList[0].name )

print("end")
