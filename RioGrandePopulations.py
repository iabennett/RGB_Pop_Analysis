# Population Aggregation from yearly raster files to the county/presidio
# level in the Rio Grande River Basin (RGB)
# Iain Bennett 4/12/2021

# Import ArcPy Package and Spatial Analyst Module

import arcpy
from arcpy import *
from arcpy.sa import *


# Retrieve Spatial Analyst License from ArcGIS License Manager

arcpy.CheckOutExtension("Spatial")


# Set Working Directory containing population raster files
# This will also be the destination for the created vector files

arcpy.env.workspace = "G:/Arcpy_Env"


# Create list containing name of each raster in working directory of type TIF
# In this case, this should be the names of the population raster datasets

rasters = ListRasters("*","TIF")


# Create list containing name of each feature class in the working directory
# In this case, this should be the name of the shapefile for counties in the RGB

counties = ListFeatureClasses()


# List of years for which to aggregate population rasters
# These will be used in naming output files

years = ["2000","2005","2010","2015","2020"]


# Iterate over list of rasters and calculate sum of raster value within each
# feature in counties using ZonalStatistics and save output to working directory

for i in range(len(rasters)):
    output = ZonalStatistics(counties[0], "FID", rasters[i], "SUM")
    output.save("countyPop"+years[i])
