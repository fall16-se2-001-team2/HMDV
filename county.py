#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Isaac Styles
# Department Name : Computer and Information Sciences
# File Name                :Parser.py
# Purpose                  :Parses a json dictionary into a county with geometry.
#
#
# Author			        : Jacob Gantt (ganttj@etsu.edu
#                                   Product Owner: Isaac Styles (styles@etsu.edu
# Create Date	            :Oct 11, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Oct 11, 2016
# Modified By		: Jacob Gantt
#
#-------------------------------------------------------------------------------------------------------------

class county:
    def __init__(self, jsonObj):
        self.jsonObj = jsonObj
        self.geo = jsonObj.get("geometry")
        self.name = jsonObj.get("name").lower()
        self.nameFull = jsonObj.get("name") + " County"

