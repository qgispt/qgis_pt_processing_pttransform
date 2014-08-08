ED50 to ETRS89-PTTM06
================================

Description
-----------

The tool take an input vector defined with the "ED50" CRS (EPSG 23029) and creates an output shapefile defined with the ETRS89-PTTM06 CRS (EPSG 3763).
Datum transformation NTv2 are used in the process, to garauntee the smallest error as possible.

Parameters
----------

- ``Input layer[Vector]``: Input vector

- ``Grid to use/origin[NTv2 Datum Transformation grid]``: Supported NTv2 grids is the ones provided by Prof. Jose Alberto Goncalves (UP)

Outputs
-------

- ``Output[Vector]``: Output vector in shapefile format