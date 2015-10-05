
import arcpy
from arcpy import env
env.workspace = "P:/PyhtonHomeWork/Data/Exercise08"
env.workspace = "P:/PyhtonHomeWork/Data/Exercise08"
env.overwriteOutput = True
outpath ="P:/PythonHomeWork/Data/Exercise08"
newfc = "Results/newpolygon.shp"

arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = "E:/UNIVERSITY/Exercise08/challengecoordinates.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line, " ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
