import arcpy
from arcpy import env
env.workspace = "P:/PythonHomeWork/Data/Exercise07"
fp = "P:/PyhtonHomeWork/Data/Exercise07/Results/airports.shp"
fp2 = "P:/PyhtonHomeWork/Data/Exercise07/Results/seaplaneairports.shp"
outfp = "P:/PythonHomeWork/Data/Exercise07/Results/air_buf.shp"
outfp2 = "P:/PythonHomeWork/Data/Exercise07/Results/sea_buf.shp"
fieldname = "FEATURE"
delimited = arcpy.AddFieldDelimiters(fp, fieldname)
arcpy.Select_analysis(fp, outfp, delimited +"='Airport'")
unique_name=arcpy.CreateUniqueName("buffer.shp")
arcpy.Buffer_analysis("airports.shp", unique_name, "15000 METERS")
arcpy.Select_analysis(fp2, outp2, delimited +"='Seaplane Base'")
arcpy.Buffer_analysis("seaplaneairports.shp", unique_name, "7500 METERS")
seaports
