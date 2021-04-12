# Rio Grande Basin Population Aggregation
Code and pseudocode for aggregating Gridded Population Data across counties in the Rio Grande Basin

## Purpose
This code was created to automate the process of calculating the population in each county in the Rio Grande Basin from 2000 to 2020, using the Gridded Population of the World, Version 4 dataset. This was a part of a research project focused on the relationship between population density and water withdrawals in the Rio Grande/Rio Bravo Basin.

## Data 
This code was initially built to use the dataset created by the Center for International Earth Science Information Network based on population counts consistent with national censuses and adjusted to match United Nations country totals. This code also initially utilized a feature class for each county in the Rio Grande/Rio Bravo Basin, compiled by Plassin et al. (2019) using data from the US Census Bureau and the Instituto Nacional de Estadística y Geografía. The data used is referenced below. 

##### Center for International Earth Science Information Network - CIESIN - Columbia University. 2018. Gridded Population of the World, Version 4 (GPWv4): Population Density Adjusted to Match 2015 Revision UN WPP Country Totals, Revision 11. Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4F47M65.
##### Plassin, S., Koch, J., Paladino, S., Friedman, J. R., Spencer, K., Vaché, K. B., 2019. Geospatial data for the Rio Grande/Río Bravo socio-environmental system. Open Science Framework. https://doi.org/10.17605/OSF.IO/79426.

## Usage
This code is built using the ArcPy package and as such will require an ArcGIS license, as well as the Spatial Analyst extension. For best results, set the working directory in the code to a folder containing only the population datasets to be aggregated (formatted as .TIF) and a feature class of the areas to aggregate (formatted as .shp). 
