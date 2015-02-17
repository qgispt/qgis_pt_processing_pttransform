Ferramentas de Transformação de Datum para a Caixa de Ferramentas de Processamento do QGIS, usando as Grelhas NTv2 de Portugal Continental
--------------------------------------

.. image :: ../icons/pttransform.png

A Caixa de Ferramentas de Processamento do QGIS (anteriormente denominada SEXTANTE), é um ambiente de geoprocessamento que pode ser usado tanto para executar algoritmos nativos do QGIS, como de softwares independentes, tornando as tarefas de análise espacial bastante mais simples e produtivas.

Este plugin permite fazer a transformação de dados vetoriais e raster dos Sistemas de Referência usados, no passado, em Portugal Continental (Datum 73, Datum Lisboa e Datum Europeu 1950) para o novo Sistema de Referência PT-TM06/ETRS89, utilizando o Método das Grelhas. Para mais informações acerca dos métodos de transformação de coordenadas consulte a seguinte entrada no blog do Grupo de Utilizadores QGIS PT: http://qgis.pt/blog/2014/07/13/transformacao-de-coordenadas-e-utilizacao-das-grelhas-ntv2-no-qgis/

O plugin disponibiliza os dois conjuntos de grelhas NTv2 existentes em Portugal Continental, deixando ao critério do utilizador a escolha de qual deverá utilizar:
- http://www.fc.up.pt/pessoas/jagoncal/coordenadas/ (elaboradas pelo Professor José Alberto Gonçalves - FCUP);
- http://www.dgterritorio.pt/cartografia_e_geodesia/geodesia/transformacao_de_coordenadas/grelhas_em_ntv2/ (elaboradas pela Direção-Geral do Território).

Essa escolha poderá ser sustentada pelos detalhes apresentados no texto supracitado.

O plugin foi criado com o objetivo de ser o mais simples possível para o utilizador: as ferramentas encontram-se organizadas, em primeiro lugar, por tipo de dados (raster ou vetor) e depois pelo Sistema de Referência dos dados de origem. 

.. image :: ../icons/pttransform_menu.png

Assim, se o utilizador pretender, por exemplo, transformar uma shapefile no Datum Lisboa para PT-TM06/ETRS89, só terá de expandir o menu "Transformação de Datum em Vectores" e executar a ferramenta "De Datum Lisboa para ETRS89-PTTM06", selecionar a shapefile de entrada, escolher a grelha NTv2 a usar (do Professor José Alberto Gonçalves ou da Direção-Geral do Território), definir o caminho para a shapefile resultante e executar a ferramenta.

.. image :: ../icons/pttransform_gui.png

Tal como qualquer outra ferramenta da Caixa de Ferramentas de Processamento, estas ferramentas podem ser executadas em lote.

O plugin foi desenvolvido por Alexander Bruy, Pedro Venâncio e NaturalGIS (http://www.naturalgis.pt/), com o suporte do Grupo de Utilizadores QGIS PT (http://www.qgis.pt/).
