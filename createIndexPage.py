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
path="./screenshots/"

pdf, placeholder = False, False
dirList=os.listdir(path)
dirList.sort(reverse=True)
output = ""
for fname in dirList:
    if fname.find("-v") != -1: versionScreenshot = True
    if versionScreenshot:
        version = fname.replace(".png","").replace("screenshot-","")
        output += "* [Screenshot of version %s](http://pklaus.github.com/Unicode-Char-Selector/screenshots/%s)\n" % (version, fname)
    	versionScreenshot = False
print output