#to be used in the Qgis application 
# a simple script of clipping in QGIS
import processing 
from qgis.core import *
import os 

#add the overlay polygon path 
polyPath="C:/Users/User/Desktop/taita taveta.shp"
#add the point or clip feature path 
pointPath='C:/Users/User/Desktop/john makoha\'s assignment/harvard-africover-ke-othertowns-shapefile/AFRICOVER_KE_OTHERTOWNS.shp'
# add the output feature path
clipPath= 'C:/Users/User/Documents/pyclips/clipped1.shp'
# run the clip 
processing.run('native:clip',{'INPUT': pointPath,'OVERLAY':polyPath,'OUTPUT':clipPath})
#add the clipped feature to the map canvas 
iface.addVectorLayer(clipPath,"",'ogr')
