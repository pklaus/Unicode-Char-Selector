#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# author: Philipp Klaus, philipp.l.klaus AT web.de


# This file is part of netio230a.
#
# netio230a is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# netio230a is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with netio230a. If not, see <http://www.gnu.org/licenses/>.


import os
BASE_PATH = "./screenshots/"
OUT_FILE = "./index.markdown"
OUT_FILE_STATIC_HEADER = """---
layout: base
title: Unicode Char Selector
---
"""
OUT_FILE_DIVIDER = """
## Screenshot of the current version

Screenshot of the current version (%s):  
![Screenshot of the current version](./screenshots/%s)

## Screenshots of previous versions

"""

pdf, placeholder = False, False
dirList = os.listdir(BASE_PATH)
dirList.sort(reverse=True)
output = OUT_FILE_STATIC_HEADER
currentVersionDisplayed = False
versionScreenshot = False
for fname in dirList:
	if fname.find("-v") != -1: versionScreenshot = True
	if versionScreenshot:
		versionScreenshot = False
		version = fname.replace(".png","").replace("screenshot-","")
		if not currentVersionDisplayed:
			output += OUT_FILE_DIVIDER % (version, fname)
			currentVersionDisplayed = True
		else:
			output += "Screenshot of version %s:  \n![Screenshot of version %s](./screenshots/%s)\n\n" % (version, version, fname)

f = open(OUT_FILE, 'w')
f.write(output)
f.close()