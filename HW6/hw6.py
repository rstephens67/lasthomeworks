import arcpy
from arcpy import env
env.workspace = "P:/ESRIPress/Python/Data/Exercise07"
sq11 = " \"FEATURE\" = 'Airport'"
sq12 = " \"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp", sq11)
arcpy.Select_analysis ("airports.shp", "Rsults/seaports.shp", sq12)
arcpy.Buffer_analysis("Results/airports_final.shp", "Results/airports_buffers.shp", "1500 METERS")
arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffer.shp", "7500 METERS")

import arcpy
from arcpy import env
env.workspace = "P:/ESRIPress/Python/Data/Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1] = "NO"
    cursor.updateRow(row)

    
