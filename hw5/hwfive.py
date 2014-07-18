import arcpy
from arcpy import env
arcpy.env.workplace = "P:/ESRIPress/Python/Data/Exercise06"
fclist = arcpy.ListFeatuerClasses()

for feature in fclist:
    myshape = arcpy.Describe(feature)
    print "{} is a {} {}".format(myshape.name, myshape.shapeType, myshape.datasetType)

arcpy.createFileGDB_management("P:/ESRIPress/Python/Data/Exercise06/Results", "NM.gdb")
for fc in fclist:
    shape = arcpy.Describe (fc)
    if shape.shapeType == u'polygon':
        arcpy.CopyFeatures_management(fc, "P:/ESRIPress/Python/Data/Exercise06/Results/NM.gbd/" + shape.basename)
        
