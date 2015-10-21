import arcpy
outraster = arcpy.sa.Slope("P:/PythonHomeWork/Data/Exercise09/Elevation")
myraster = arcpy.Raster("P:/PythonHomeWork/Data/Exercise09/Elevation")
import arcpy

arcpy.env.workspace = ("P:/PythonHomeWork/Data?Exercise09/Landcover.tif")
featureClassList = arcpy.ListFeatureClasses()
clipFeature = ("P:/PythonHomeWork/Data/Exercise09/Landcover.tif")

for featureClass in featureClassList:
    arcpy.Clip_analysis(featureClass, clipFeature, ("P:/PythonHomeWork/Data/Exercise09/Landcover.tif") + featureClass)
arcpy.raster.save_outraster
