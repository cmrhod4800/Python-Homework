def CH10():
    import arcpy
    mxd = "P:/PythonHomeWork/Data/Exercise10/AustinTX.mxd"
    mapdoc = arcpy.mapping.MapDocument(mxd)
    dfs = arcpy.mapping.ListDataFrames(mapdoc)
    lyrlist = arcpy.mapping.ListLayers(mapdoc)
    for lyr in lyrlist:
        if lyr.name == "parks":
            for df in dfs:
                if lyr in df == "parks":
                    print "Skipped"
                else:
                    arcpy.mapping.AddLayer(df, lyr, "BOTTOM")
    
