def fc2df (fc, fields=None):
    """Returns a df based on a Feature Class. Uses Cursor"""
    if fields:
        in_fields = fields
    else:
        in_fields = [str(field.name) for field in arcpy.ListFields(fc)]

    cursor = arcpy.da.SearchCursor(fc,in_fields)
    data = [row for row in cursor ]
    df = pd.DataFrame (data,columns=in_fields)

    return df
  
  
  def fc2df (fc, fields):
    """Returns a df based on a Feature Class. Uses Numpy"""
        if fields:
        in_fields = fields
    else:
        in_fields = [str(field.name) for field in arcpy.ListFields(fc)]
        
    arr = arcpy.da.FeatureClassToNumPyArray(
                in_table=fc,
                field_names=in_fields,
                skip_nulls=False,
                null_value=-99999)

    df = pd.DataFrame (arr)

    return df
