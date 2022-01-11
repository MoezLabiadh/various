var tko_limits = ee.FeatureCollection("users/labiadhmoez/tko");

var l8 = ee.ImageCollection("COPERNICUS/S2");

var l8_preFire = l8.filterDate('2018-05-01', '2018-06-30').mean();
var l8_postFire = l8.filterDate('2018-08-01', '2018-08-31').mean();

var l8_tko_preFire = ee.Image(l8_preFire.clip(tko_limits));
var l8_tko_postFire = ee.Image(l8_postFire.clip(tko_limits));


var nir = l8_tko_preFire.select('B8');
var swir = l8_tko_preFire.select('B12');
var preFireNBR = nir.subtract(swir).divide(nir.add(swir));

var nir = l8_tko_postFire.select('B8');
var swir = l8_tko_postFire.select('B12');
var postFireNBR = nir.subtract(swir).divide(nir.add(swir));

var dNBR = preFireNBR.subtract(postFireNBR);

var ndviParams = {min: -0.1, max: 0.6, palette: ['green', 'yellow', 'orange', 'red']};
Map.addLayer(dNBR,ndviParams, 'dNBR');
