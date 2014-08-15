<<<<<<< HEAD:help/dedatum73parapttm06etrs89.rst
Datum 73 Militar to ETRS89-PTTM06
=======
De Datum Lisboa para PT-TM06/ETRS89
>>>>>>> b6b6b43ec296e20ed1b33fbe7c0dc6473fb8cb4f:help/fromdatumlisboatoetrs89pttm06.rst
================================

Descrição
-----------

<<<<<<< HEAD:help/dedatum73parapttm06etrs89.rst
The tool takes an input vector layer defined with the "Datum 73 Militar" CRS (ESRI 102160) and creates an output shapefile defined with the ETRS89-PTTM06 CRS (EPSG 3763).
Datum transformation NTv2 are used in the process, to guarantee the smallest error as possible.
=======
Esta ferramenta usa como ficheiro de entrada um vector em "Datum Lisboa" (ESRI 102165 - EPSG 20791). O ficheiro de saída será um shapefile no Sistema de Referência PT-TM06/ETRS89 (EPSG: 3763) (EPSG 3763).
>>>>>>> b6b6b43ec296e20ed1b33fbe7c0dc6473fb8cb4f:help/fromdatumlisboatoetrs89pttm06.rst


Parâmetros
----------

- ``Ficheiro de entrada [Vector]``: vector de entrada

- ``Grelhas NTv2 [de transformação de Datum] a usar (Fonte)``: Escolher uma das duas grelhas NTv2 suportadas - as desenvolvidas pelo Prof. José Alberto Gonçalves, da Faculdade de Ciências da Universidade do Porto (FCUP) ou as produzidas pela Direção-Geral do Território (DGT).


Ficheiros de saida
-------

- ``Ficheiro de saída [Vector]``: vector de saída em formato shapefile

