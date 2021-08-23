import os
import arcpy

def sdeConnections():
    appdata = os.getenv('APPDATA')
    arcgisVersion = arcpy.GetInstallInfo()['Version']
    arcCatalogPath = os.path.join(appdata ,'ESRI',u'Desktop'+'10.6', 'ArcCatalog')
    sdeConnections = []
    for file in os.listdir(arcCatalogPath):
        fileIsSdeConnection = file.lower().endswith(".sde")
        if fileIsSdeConnection:
            sdeConnections.append(os.path.join(arcCatalogPath, file))
    print (sdeConnections)
    return sdeConnections

sdeConnections()
