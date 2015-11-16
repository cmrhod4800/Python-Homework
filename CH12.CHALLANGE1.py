import arcpy
def countstringfields(layer = "streets.shp"):
    arcpy.env.workspace = "P:PythonHomeWork/Data/Exercise12"
    if layer == none:
        return none
    n = 0
    for field in arcpy.listfieldds(layer):
        if field.type == "string":
            n =+ 1
    
