#-------------------------------------------------------------------------------
# Name:     Imagery Tile Index Creator

# Purpose: This tool creates raster tile (footprint) indexes.
#          User inputs are the directory contatining the rasters/images
#         (may contain sub-folders) and the Feature Class FC or Shapefile
#         to which the raster extents will be added.
#         The input FC must have a field called "location"
#         that will hold the path to each raster tile.
#
# Author:  Moez Labiadh, BCTS-TKO
#
# Created: 04-11-2020
#-------------------------------------------------------------------------------


import os
import arcpy
from itertools import combinations


def list_img_files (search_dir):
    """Returns a list of all image files inside a given search directory"""
    theList =[]
    # loop through folders and sub-folders and retrieve all image files
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if (file.endswith(".tif") or file.endswith(".ecw")) and not file.startswith('Ov'):
                file_path = os.path.join(root, file)
                theList.append (file_path)
    '''
    # (if required) remove duplicates based on conditions
    # in this case ECW duplicates are removed if TIF exists
    comb = combinations(theList, 2)
    for x, y in comb:
        if os.path.basename (x)[0:12] == os.path.basename (y)[0:12]:
            if x.endswith('.ecw'):
                theList.remove(x)
            elif y.endswith('.ecw'):
                theList.remove(y)
            else:
                pass
    '''
    print ('{} images found in the serach directory' .format(len(theList)))

    return theList


def create_index_file (img_list, feature_class):
    """Returns the index Feature Class (or shapefile)based on on a list
       of image files"""
    counter = 1
    for file in img_list:
        print ('Adding raster {} of {}' .format (counter, len(img_list)))
        counter +=1
        # read each image file as raster
        raster = arcpy.sa.Raster(file)

        # get the extent of each image file
        extent = raster.extent
        XMAX = extent.XMax
        XMIN = extent.XMin
        YMAX = extent.YMax
        YMIN = extent.YMin

        # create a polygon geometry based on the extent coordinates
        pnt1 = arcpy.Point(XMIN, YMIN)
        pnt2 = arcpy.Point(XMIN, YMAX)
        pnt3 = arcpy.Point(XMAX, YMAX)
        pnt4 = arcpy.Point(XMAX, YMIN)

        array = arcpy.Array()
        array.add(pnt1)
        array.add(pnt2)
        array.add(pnt3)
        array.add(pnt4)
        array.add(pnt1)

        spatial_ref = arcpy.Describe(raster).spatialReference
        polygon = arcpy.Polygon(array, spatial_ref)

        # append the polygon to the index feature class
        cursor = arcpy.da.InsertCursor(feature_class, ["SHAPE@","location"])
        cursor.insertRow([polygon, str(file)])

    del cursor
    print ('Processing Completed!')


def main ():
    """ Runs the tool"""
    # new or existing feautre class or shp to which extents will be added
    feature_class = r'\\fileserver3.nrscloud.bcgov\bcts\Data\TKO\Imagery\FTBO\FTBO_Imagery_Products.gdb\FTBO_utm_imagery_tiles_nov2020'
    # search directory
    search_dir = r'\\fileserver3.nrscloud.bcgov\bcts\Data\TKO\Imagery\FTBO\KettleEast_2014\RGB'

    # run the functions
    img_list = list_img_files (search_dir)
    create_index_file (img_list, feature_class)


main()
