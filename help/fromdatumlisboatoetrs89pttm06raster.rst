Datum Lisboa to ETRS89-PTTM06
================================

Description
-----------

The tool take an input raster defined with the "Datum Lisboa" CRS (ESRI 102165 or EPSG 20791) and creates an output geotiff defined with the ETRS89-PTTM06 CRS (EPSG 3763).
Datum transformation NTv2 are used in the process, to garauntee the smallest error as possible.

Parameters
----------

- ``Input layer[Raster]``: Input raster

- ``Grid to use/origin[NTv2 Datum Transformation grid]``: Supported NTv2 grids are the ones provided by Prof. Jose Alberto Goncalves (UP) and the ones provided by the Direcao-Geral do Territorio (DGT)

Outputs
-------

- ``Output[Raster]``: Output raster in Geotiff format