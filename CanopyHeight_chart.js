// Import BC limits shapefile
var BC_BAs = ee.FeatureCollection("users/labiadhmoez/BCTS_BAs");
// Import the Canopy Height dataset
var CanopyHeight = ee.Image("NASA/JPL/global_forest_canopy_height_2005").clip(BC_BAs);
// Add the Canopy Height to the map view and adjust visualisation parameters
Map.addLayer(CanopyHeight,
  {min: 0, max: 32, palette: ['FFFFFF', 'FEFFDE', 'FDFFAF','ECFF00', 'DFF007', 'C2EE19', 'A5E119',
                              '83DA19', '54C61A', '409D11', '4A8B29' , '3F662B', '23422D']},'Canopy Height');
//Set the Chart options
var options = {
  title: 'Average Canopy Height per BCTS Business Area',
  hAxis: {title: 'Canopy Height (m)'},
  vAxis: {title: 'Business Area'}};
//Set the Chart parameters
var chart = ui.Chart.image.byRegion({
  image: CanopyHeight,
  regions: BC_BAs,
  reducer: ee.Reducer.mean(),
  scale: 500,
  xProperty: 'code'
}).setOptions(options)
  .setChartType('BarChart');
// Display the Chart.
print(chart);
