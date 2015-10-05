import arcpy
from arcpy import env
env.workspace = "P:/PythonHomeWork/Data/Exercise08"
fc = "Hawaii.shp"
fc = r"P:/PythonHomeWork/Data/Exercise08/Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@","SHAPE@","SHAPE@AREA","SHAPE@LENGTH"])
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
