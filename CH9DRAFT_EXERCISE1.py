import arcpy
from arcpy import env
from arcpy.sa import * 
env.workspace = "P:/PythonHomeWork/Data/Exercise09"
arcpy.CheckOutExtension("spatial")
outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")
arcpy.CheckInExtension("spatial")
moderate_slope == ({5}, +{20})
southernly_aspect == ({150}, +{270})
outreclass = Reclassify("elevation", "VALUE", myremap)
outreclass.save("elev_recl")
myremap == arcpy.sa.ElevRemapValue([[41,1], + [42,2], + [43,3]])
outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
outreclass.save("lc_recl")
