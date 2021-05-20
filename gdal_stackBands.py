import os
from osgeo import gdal


Workspace = 'H:/Profile/Desktop/TRAINING/RS/SnowCoverProject'
workspace2 = r'F:\tko_root\GIS_WORKSPACE\MLABIADH\PyMe\MachineLearning'
S2_path = os.path.join (Workspace, 'raw_data/S2B_MSIL2A_20191208T184749_N0213_R070_T11UNQ_20191208T205518.SAFE')

#Browse through the S2 product folder and retrieve the required bands.
S2_bands = []

for root, dirs, files in os.walk(S2_path):
    for name in files:
        if name.endswith("B02_10m.jp2"):
            Bpath = os.path.join (root, name)
            S2_bands.append(Bpath)
        elif name.endswith("B03_10m.jp2"):
            Gpath = os.path.join (root, name)
            S2_bands.append(Gpath)
        elif name.endswith("B04_10m.jp2"):
            Rpath = os.path.join (root, name)
            S2_bands.append(Rpath)
        elif name.endswith("B08_10m.jp2"):
            NIRpath = os.path.join (root, name)
            S2_bands.append(NIRpath)            
        elif name.endswith("B11_20m.jp2"):
            SWIR1path = os.path.join (root, name)
            S2_bands.append(SWIR1path)
        elif name.endswith("B12_20m.jp2"):
            SWIR2path = os.path.join (root, name)  
            S2_bands.append(SWIR2path)

        else:
            pass
      
print ('Bands retrieved from the Sentinel-2 imagery folder')

#Stack the bands into a Composite Image
outvrt = '/vsimem/stacked.vrt' #/vsimem is special in-memory gdal virtual "directory"
outtif = os.path.join (workspace2, 'inputs','S2A_' + os.path.basename(Gpath)[:15] + '_Band_Composite.tif')

outds = gdal.BuildVRT(outvrt, S2_bands, separate=True)
outds = gdal.Translate(outtif, outds)

print (' S2 Band Composite created')