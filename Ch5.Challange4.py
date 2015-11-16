import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise05"
if arcpy.CheckExtension("3DAnalyst") == "Available":
    print "3D Analyst available."
else:
    print "3D Analyst not available" 
if arcpy.CheckExtension("NetworkAnalyst") == "Available":
    print "Network Analyst available."
else:
    print "Network Analyst not available"
if arcpy.CheckExtension("Spatial") == "Available":
    print "Spatial available."
else:
     print "Spatial not available"
