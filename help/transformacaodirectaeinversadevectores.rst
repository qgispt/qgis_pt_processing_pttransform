Transformação Directa e Inversa de Vectores
================================

Descrição
-----------

Esta ferramenta usa como ficheiro de entrada um vector. O ficheiro de saída será um shapefile. A transformação de datum com as grelhas NTv2 pode ser efectuada na forma directa (Data nacionais antigos [Datum Lisboa / Datum Lisboa Militar / Datum 73 / Datum 73 Militar / ED50 UTM 29N] ->  PT-TM06/ETRS89) ou na forma inversa (PT-TM06/ETRS89 -> Data nacionais antigos [Datum Lisboa / Datum Lisboa Militar / Datum 73 / Datum 73 Militar / ED50 UTM 29N]).


Parâmetros
----------

- ``Ficheiro de entrada [Vector]``: vector de entrada

- ``Transformação``: Escolher entre as formas de transformação disponibilizadas - [Directa] para transformações dos data nacionais antigos (Datum Lisboa / Datum Lisboa Militar / Datum 73 / Datum 73 Militar / ED50 UTM 29N) para o PT-TM06/ETRS89; [Inversa] para transformações do PT-TM06/ETRS89 para um dos data nacionais antigos (Datum Lisboa / Datum Lisboa Militar / Datum 73 / Datum 73 Militar / ED50 UTM 29N).

- ``Datum antigo``: Escolher o datum nacional antigo do ficheiro de entrada, para o caso de transformações na forma directa. Para transformações na forma inversa, esta opção corresponde ao datum a aplicar ao ficheiro de saída.

- ``Grelhas NTv2 [de transformação de datum] a usar (Fonte)``: Escolher uma das duas grelhas NTv2 suportadas - as desenvolvidas pelo Prof. José Alberto Gonçalves, da Faculdade de Ciências da Universidade do Porto (FCUP), ou as produzidas pela Direção-Geral do Território (DGT). A DGT não disponibiliza grelhas para o ED50 UTM 29N, pelo que para dados nesse sistema, a transformação usa sempre as grelhas do Prof. José Alberto Gonçalves.


Ficheiros de saída
-------

- ``Ficheiro de saída [Vector]``: vector de saída em formato shapefile
