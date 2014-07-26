Mainland Portugal Datum Transformation tools for the QGIS Processing toolbox
--------------------------------------

![](../icons/pttransform.png)

Processing (former SEXTANTE) is a geoprocessing environment that can be used to call native and third party algorithms from QGIS, making your spatial analysis
tasks more productive and easy to accomplish.

This plugin allows easy datum transformations from obsolete mainland Portugal CRSs (Datum 73, Datum Lisboa and ED50) to the new official CRS 
(ETRS89-PTTM06) using NTv2 datum transformation grids.

Supported NTv2 grids are the ones provided by Prof. José Alberto Gonçalves and the ones provided by the Direção-Geral do Território (DGT), see:

http://www.fc.up.pt/pessoas/jagoncal/coordenadas/

http://www.dgterritorio.pt/cartografia_e_geodesia/geodesia/transformacao_de_coordenadas/grelhas_em_ntv2/

The grids files are shipped with the plugin, so no further actions are required by the user.

The plugin was made to be as simpliest as it can be for the user: the tools are organized first by data type (raster or vector) and then by origin CRS (Datum 73 or Datum Lisboa or ED50). 

![](../icons/pttransform_menu.png)

Then the user just selects the input layer and the grid he/she want to use.

![](../icons/pttransform_gui.png)

As any other tool in the Processing toolbox this tools can be run in batch mode.

The plugin was developed by Alexander Bruy, Pedro Venâncio and Faunalia (http://www.faunalia.eu/) with the support of the Portugal QGIS User Group (http://www.qgis.pt/).