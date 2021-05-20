import arcpy
import pandas as pd
from datetime import datetime, timedelta
import datetime

dem = r'\\imagefiles.bcgov\dem\elevation\trim_25m\bcalbers\tif\bc_elevation_25m_bcalb.tif'

val_dict = {}
val_dict ['BLOCK_NBR'] = []
val_dict ['LICENCE_ID'] = []
val_dict ['BLOCK_ID'] = []
val_dict ['UBI'] = []
val_dict ['CUTB_LOCATION'] = []
val_dict ['LICN_SEQ_NBR'] = []
val_dict ['Elevation']= []
val_dict ['Area (ha)']= []
val_dict ['Sold ?']= []
val_dict ['Ad date']= []

mxd_path = r'\\BCTSdata.bcgov\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\harold_tool\consultation_tracker_v2.mxd'
mxd = arcpy.mapping.MapDocument(mxd_path)

for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "FORESTVIEW.SV_BLOCK":
        block_lyr = lyr
        fields = ['BLOCK_NBR' , 'LICENCE_ID', 'BLOCK_ID' , 'CUTB_LOCATION' , 'LICN_SEQ_NBR','SHAPE@AREA', 'SHAPE@XY', 'UBI']
        cursor = arcpy.da.SearchCursor(block_lyr,fields)
        for row in cursor:
            val_dict ['BLOCK_NBR'].append(row[0])
            val_dict ['LICENCE_ID'].append(row[1])
            val_dict ['BLOCK_ID'].append(row[2])
            val_dict ['UBI'].append(row[7])
            val_dict ['CUTB_LOCATION'].append(row[3])
            val_dict ['LICN_SEQ_NBR'].append(int(row[4]))
            val_dict ['Area (ha)'].append(round(row[5]/10000,2))

            pnt = arcpy.Point(row[6][0],row[6][1])
            ptGeometry = arcpy.PointGeometry(pnt)
            arcpy.Buffer_analysis(ptGeometry, 'in_memory\ptBuf', 100)
            extent = arcpy.Describe('in_memory\ptBuf').extent
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
            elevation = rstArray[arow,acol]
            val_dict ['Elevation'].append(elevation)

            arcpy.Delete_management("in_memory")

val_dict ['Sold ?'].extend('No' for i in range(len(val_dict ['LICN_SEQ_NBR'])))
val_dict ['Ad date'].extend('n/a' for i in range(len(val_dict ['LICN_SEQ_NBR'])))

for tab in arcpy.mapping.ListTableViews(mxd):
    if tab.name == "FORESTVIEW.V_LICENCE_ACTIVITY_ALL":
        lic_act_tab = tab
        fields = ['LICN_SEQ_NBR', 'ACTI_STATUS_IND' , 'ACTI_STATUS_DATE' ]
        cursor = arcpy.da.SearchCursor(lic_act_tab,fields)

        for row in cursor:
            for i in range(0, len(val_dict ['LICN_SEQ_NBR'])):
                if row[0] == val_dict ['LICN_SEQ_NBR'][i]:
                    if row[1] == 'D':
                        val_dict['Sold ?'][i] = 'Yes'
                    if row[2] is not None:
                        lic_act_date = row[2]
                        ad_date = lic_act_date - timedelta(days=28)
                        val_dict ['Ad date'][i] =  ad_date.strftime("%Y/%m/%d")

print ({k:len(v) for k, v in val_dict.items()})

df = pd.DataFrame.from_dict(val_dict)
print (df.head())

order_cols = ['BLOCK_NBR', 'LICENCE_ID', 'BLOCK_ID', 'UBI', 'CUTB_LOCATION', 'Area (ha)', 'Elevation', 'Sold ?', 'Ad date', 'LICN_SEQ_NBR']
df = df[order_cols]
#df.drop(columns=['LICN_SEQ_NBR'])

df.sort_values(by=['LICENCE_ID'], inplace=True)
df = df.reset_index(drop=True)

df.index = df.index + 1
df.index.name = '#'

out_excel = r'\\bctsdata.bcgov\data\tko_root\GIS_WORKSPACE\MLABIADH\GIS-REQUESTS\harold_tool\consult_tracker_info.xlsx'
df.to_excel(out_excel)