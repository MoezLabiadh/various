import os
import arcpy
from arcpy.sa import*
import numpy as np
arcpy.CheckOutExtension("Spatial")
workspace = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\overlay_tool\inputs.gdb'
block = os.path.join(workspace, 'test_roads')
dem = r'\\imagefiles.bcgov\dem\elevation\trim_25m\bcalbers\tif\bc_elevation_25m_bcalb.tif'

sr = arcpy.Describe(dem).spatialReference

cursor = arcpy.da.SearchCursor(block,["SHAPE@XY"],'',sr)
for row in cursor:
        pnt = arcpy.Point(row[0][0],row[0][1])
        ptGeometry = arcpy.PointGeometry(pnt)

        arcpy.Buffer_analysis(ptGeometry, 'in_memory\ptBuf', 100)
        extent = extent = arcpy.Describe('in_memory\ptBuf').extent
        arcpy.Clip_management(dem, str(extent), 'in_memory\dem')

        rast = arcpy.Raster('in_memory\dem')
        desc = arcpy.Describe(rast)
        ulx = desc.Extent.XMin
        uly = desc.Extent.YMax
        rstArray = arcpy.RasterToNumPyArray(rast)

        deltaX = pnt.X - ulx
        deltaY = uly- pnt.Y
        arow = int(deltaY/rast.meanCellHeight)
        acol = int(deltaX/rast.meanCellWidth)
        data = rstArray[arow,acol]
        print(data)
        arcpy.Delete_management("in_memory")


#####################################
#########################################

    arcpy.CheckOutExtension("Spatial")
    dem = dem = r'\\imagefiles.bcgov\dem\elevation\trim_25m\bcalbers\tif\bc_elevation_25m_bcalb.tif'
    arcpy.FeatureToPoint_management(features, 'in_memory\centroid',
                                    "CENTROID")
    ExtractValuesToPoints('in_memory\centroid', dem,
                          'in_memory\elev',"INTERPOLATE")
    val_dict['Elevation']= [int(row[0]) for row in arcpy.da.SearchCursor('in_memory\elev', ['RASTERVALU'])]