import arcpy

fc = r'\\sfp.idir.bcgov\S164\S63087\Share\FrontCounterBC\Moez\20210607_proximity_analysis\gis\data.gdb\linked'


fields = ['CROWN_LANDS_FILE', 'TENURE_STAGE', 'TENURE_STATUS']
values = [r[0] for r in arcpy.da.SearchCursor(fc,fields)]

duplicate = []
with  arcpy.da.SearchCursor(fc,fields) as cursor:
        for row in cursor:
            if values.count(row[0]) > 1:
                duplicate.append (row[0])


dup_removed = list(dict.fromkeys(duplicate))
