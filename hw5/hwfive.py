import arcpy
from arcpy import env
arcpy.env.workplace = path
fclist = arcpy.ListFeatuerClasses()

for feature in fclist:
    myshape = arcpy.Describe(fclist)
