import ee
from ee_plugin import Map

#Define the Area of Interest
AOI =  ee.Geometry.Polygon(
        [[[-119.72914023450834, 51.64737044195003],
          [-119.72914023450834, 49.004039123940004],
          [-114.22498984388334, 49.004039123940004],
          [-114.22498984388334, 51.64737044195003]]])
          
#Define dates
date_start = '2020-05-03'
date_end= '2020-06-03'

#Define a Cloud Threshold
cloud_threshold = 20

# Function for masking Clouds
def maskS2clouds(image):
    qa = image.select('QA60')
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11
    mask = qa.bitwiseAnd(cloudBitMask).eq(0)\
      and(qa.bitwiseAnd(cirrusBitMask).eq(0))
    return image.updateMask(mask).divide(10000)


#Setup a function to caclulate the NDVI
def CalculateNDVI(image):
    NDVI = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    return image.addBands(NDVI)
        
        
#Add Sentinel-2 Collection and filter using AOI, dates, cloud threshold.
S2 = ee.ImageCollection("COPERNICUS/S2_SR")\
      .filterDate(date_start, date_end)\
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloud_threshold))\
      .sort('system:time_start')\
      .filterBounds(AOI)\
      .map(maskS2clouds)\
      .map(CalculateNDVI)

S2image = S2.min()

S1 = ee.ImageCollection('COPERNICUS/S1_GRD')\
   .filterBounds(AOI)\
   .filterDate(date_start, date_end)\
   .select('VV')

S1image = S1.median().int32()
glcm = S1image.glcmTexture();
contrast = glcm.select('VV_savg')

#Set the visualisation parameters.
NdviVizParam = {
  'min': 0,
  'max': 1,
  'palette': [
    'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
    '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
    '012E01', '011D01', '011301'
  ],
}

S2Viz = {
  'min': 0,
  'max': 0.15,
  #'gamma': [0.95, 1.1, 1]
}

S1Viz = {
  'min': -25,
  'max': 10
}

ContrastViz = {
  'min': -25,
  'max': -10, 
  'palette': ['yellow', 'green', 'orange', 'red', 'blue', 'purple']
}

Map.setCenter (-117.30,49.50,10)
#Map.addLayer(contrast, ContrastViz, 'Contrast')
#Map.addLayer(S1image, S1Viz, 'Sentinel-1 imagery')
Map.addLayer(S2image.select('B4', 'B3', 'B2').clip(AOI), S2Viz, 'Sentinel-2 imagery')
#Map.addLayer(image.select('NDVI').clip(AOI), NdviVizParam, 'Vegetation Index');