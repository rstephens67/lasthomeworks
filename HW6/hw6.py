import arcpy
arcpy.env.workspace = "P:/ESRIPress/Python/Data/Exercise07"
arcpy.Buffer_analysis("airports", "P:/ESRIPress/Python/Data/Exercise07/airports_Buffer_1", "15000 meter", "FULL", "ROUND", "LIST", "FEATURE")

import arcpy
from arcpy import env
env.workspace = "P:/ESRIPress/Python/Data/Exercise07/roads.shp"
data = env.workspace.realines()
del env.workspace

for line in data:
    line = line.split(',')
    for feature in line[8]:
        if feature.lower() == "ferry":
            print("YES")
        else:
            print("NO")
            

