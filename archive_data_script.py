'''

This Script archives an LRM block and its associated layers into an inhouse Geodatabase
User inputs are Licence, Block ID and Block State

'''

import arcpy
import sys
from datetime import date

#Paths to the MXD and Archive Geodataabse
mxdPath = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\archive_data\archive_proj_all.mxd'
archiveGDB = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\archive_data\Free_Growing_WO.mdb'

#List the FCs in the archive GDB
arcpy.env.workspace = archiveGDB
archiveFCs = arcpy.ListFeatureClasses('','','Genus')

arcpy.env.overwriteOutput = True

#This setting will make the joined and non-joined field names match (tableName.fieldName == fieldName).
arcpy.env.qualifiedFieldNames = False

#List the layers in the MXD
mxd = arcpy.mapping.MapDocument(mxdPath)
df = arcpy.mapping.ListDataFrames(mxd, '')[1]
layers = arcpy.mapping.ListLayers(mxd, '', df)

#User inputs
searchLicence = 'A86467'
searchBlock = '1'
BlockState = "FG"

#Function to retrieve the Sequence Number of  the block based on the user inputs (Licence and Block ID)
def FindSeqNum (searchLicence, searchBlock):
    fields = ['LICENCE_ID', 'BLOCK_ID', 'CUTB_SEQ_NBR']
    with arcpy.da.SearchCursor(layers[0], fields) as cursor:
        uniqueID = None
        for row in cursor:
            if (row[0] == searchLicence) and (row[1] == searchBlock):
                uniqueID = int(row[2])

    return uniqueID

#Function to copy all associated layers into the archive Geodataabse
def CopyFeatures (uniqueID):
    for lyr in layers:
        desc = arcpy.Describe(lyr)
        fields =  desc.fields
        for field in fields:
            if (str(field.name) == "CUTB_SEQ_NBR"):
                IDfield = field.name

        selectionLyr = r"in_memory\Selected"
        if arcpy.Exists(selectionLyr):
            arcpy.Delete_management(selectionLyr)

        print ("Searching for features in {}." .format(lyr))
        selectClause = str(IDfield)  + ' = ' + str(uniqueID)
        arcpy.Select_analysis(lyr, selectionLyr, selectClause)
        countSelected = (int(arcpy.GetCount_management(selectionLyr).getOutput(0)))
        print ("The {0} layer has {1} shape(s)." .format(lyr, countSelected))

        if countSelected > 0:
            arcpy.AddField_management(selectionLyr, "Date_Archived", "DATE")
            arcpy.AddField_management(selectionLyr, "Block_state", "TEXT", "", "", 50)

            todayDate = date.today().strftime("%Y-%m-%d")

            arcpy.CalculateField_management(selectionLyr, "Date_Archived", "'{}'".format (todayDate), "PYTHON_9.3")
            arcpy.CalculateField_management(selectionLyr, "Block_state","'{}'".format (BlockState), "PYTHON_9.3")

            for fc in archiveFCs:
                if str(lyr).split(".")[1] == str(fc):
                   print ("Copying shapes into {}...in progress" .format(fc))
                   arcpy.Append_management(selectionLyr, fc, "NO_TEST")


            arcpy.Delete_management(selectionLyr)

    print ("Processing Completed")


#-----------------------------#
# Run the tool
#-----------------------------#

if (FindSeqNum(searchLicence, searchBlock)) != None:
    print ("Block Sequence Number is {}. Processing started..." .format(FindSeqNum(searchLicence, searchBlock)))
    CopyFeatures (FindSeqNum(searchLicence, searchBlock))
else:
    print(" No Block Sequence Number found. Tool stopped working.")
    sys.exit()