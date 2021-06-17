import arcpy

tenures= r"\\sfp.idir.bcgov\S164\S63087\Share\FrontCounterBC\Moez\WORKSPACE\20210607_proximity_analysis\gis\data.gdb\test_subset"
zones = r"\\sfp.idir.bcgov\S164\S63087\Share\FrontCounterBC\Moez\DATASETS\local_data.gdb\Admin\district_regional_areas"

tenure_cursor = arcpy.da.SearchCursor(tenures, ['SHAPE@','CROWN_LANDS_FILE'])
for row in tenure_cursor:
    tenure_geometry = tenure_cursor[0]
    tenure_dict= {}
    distance_dict = {}

    zone_cursor = arcpy.da.SearchCursor(zones, ['SHAPE@','Zone'])
    for row in zone_cursor:
        zone_geometry = zone_cursor[0]
        dist = tenure_geometry.distanceTo(zone_geometry)
        distance_dict ['ZONE ' + str(zone_cursor[1])] = round(dist,2)

    tenure_dict [str(tenure_cursor[1])] = distance_dict

    nearest_zone = min(distance_dict, key=lambda k: distance_dict[k])
    print ('closest zone to {} is {} '.format (str(tenure_cursor[1]),nearest_zone))
