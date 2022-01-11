// Add Sentinel-2 Prefire and postfire images
var S2_preFire = ee.Image('COPERNICUS/S2/20180719T184919_20180719T185932_T11UNQ');
var S2_postFire = ee.Image('COPERNICUS/S2/20190726T183921_20190726T184401_T11UNQ');

// Calculate Normalized Burn Ratio (NBR) for each date based on Bands NIR (B5) and SWIR (B12)
var nir = S2_preFire.select('B8');
var swir = S2_preFire.select('B12');
var preFireNBR = nir.subtract(swir).divide(nir.add(swir));
var nir = S2_postFire.select('B8');
var swir = S2_postFire.select('B12');
var postFireNBR = nir.subtract(swir).divide(nir.add(swir));

// Calculate the Difference Normalized Burn Index (dNBR)
var dNBR = preFireNBR.subtract(postFireNBR);

// set visulatisation intervals (Enhanced Regrowth-Unburned-Low Severity-Medium Severity-High Severity)
var vizParam =
  '<RasterSymbolizer>' +
    '<ColorMap  type="intervals" extended="false" >' +
      '<ColorMapEntry color="#3FC426" quantity="-0.1" label="Enhanced Regrowth"/>' +
      '<ColorMapEntry color="#E1F115" quantity="0.2" label="Unburned" />' +
      '<ColorMapEntry color="#EEC418" quantity="0.4" label="Low Severity" />' +
      '<ColorMapEntry color="#E45A1E" quantity="0.7" label="Moderate Severity" />' +
      '<ColorMapEntry color="#9B2929" quantity="2" label="High Severity" />' +
    '</ColorMap>' +
  '</RasterSymbolizer>';

// Add the dNBR layer to the map view  
Map.addLayer(dNBR.sldStyle(vizParam), {}, 'dNBR');

