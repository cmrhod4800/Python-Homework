import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/PythonHomeWork/Data/Exercise08"
c = "P:/PythonHomeWork/Data/Exercise08/Hawaii.shp"
units = arcpy.Describe(fc).spatialReference.linearUnitName
 
 
for row in cursor:
    print "Total Area: ", row[2]
    print("Feature {0}: ".format(row[0]))
    partnum = 0
    perimeter = 0
    for part in row[1]:
        print("Part {0}: ".format(partnum))
        for point in part:
            perimeter += row[3]
        partnum += 1
        #print "Area: ", row[2]
        print "Perimeter: ", perimeter, units
