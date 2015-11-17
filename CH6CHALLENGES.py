
#This is Challange number one for Chapter six
import arcpy
from arcpy import env
env.workspace = "P:/PythonHomework/Data/Exercise06"
fclist = arcfpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: "" + fcdescribe.name
    print "Data type: " = fcdescribe.dataType
#This is Challange number two for Chapter six 
import arcpy
from arcpy import env
env.workspace = "P:/PythonHomework/Data/Exercise06"
arcpy.CreateFileGDB_management("P:/PythonHomework/Data/Exercise06/Results", "NM.gdb”)
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "P:/PythonHomework/Data/Exercise06/Results/NM.gdb/" + fcdesc.basename)
