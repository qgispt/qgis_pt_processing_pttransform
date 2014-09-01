# -*- coding: latin-1 -*-

"""
***************************************************************************
    VectorETR89PTTM06DirInv.py
    ---------------------
    Date                 : August 2014
    Copyright            : (C) 2014 by Pedro Venâncio
    Email                : pedrongvenancio at yahoo dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Pedro Venâncio'
__date__ = 'August 2014'
__copyright__ = '(C) 2014, Pedro Venâncio'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from PyQt4.QtGui import *

from qgis.core import *

try:
    from processing.parameters.ParameterVector import ParameterVector
    from processing.parameters.ParameterSelection import ParameterSelection
    from processing.outputs.OutputVector import OutputVector
except:
    from processing.core.parameters import ParameterVector
    from processing.core.parameters import ParameterSelection
    from processing.core.outputs import OutputVector

from processing.tools.system import *

from processing.algs.gdal.OgrAlgorithm import OgrAlgorithm
from processing.algs.gdal.GdalUtils import GdalUtils


class VectorETR89PTTM06DirInv(OgrAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    TRANSF = 'Transformação'
    TRANSF_OPTIONS = ['Directa: Data Antigos -> PT-TM06/ETRS89 [EPSG:3763]',
                      'Inversa: PT-TM06/ETRS89 [EPSG:3763] -> Data Antigos']
    CRS = 'CRS'
    CRS_OPTIONS = ['Datum Lisboa [EPSG:20791 / EPSG:5018 / ESRI:102165]',
                   'Datum Lisboa Militar [EPSG:20790 / ESRI:102164]',
                   'Datum 73 [EPSG:27493 / ESRI:102161]',
                   'Datum 73 Militar [ESRI:102160]',
                   'ED50 UTM 29N [EPSG:23029] (Só grelha do José Alberto Gonçalves)']
    GRID = 'GRELHAS'
    GRID_OPTIONS = ['José Alberto Gonçalves',
                    'Direção-Geral do Territorio']

    def getIcon(self):
        return  QIcon(os.path.dirname(__file__) + '/icons/pttransform.svg')

    def defineCharacteristics(self):
        self.name = 'Transformação Directa e Inversa de Vectores'
        self.group = 'Transformação Directa e Inversa'
        self.addParameter(ParameterVector(self.INPUT, 'Ficheiro de Entrada',
                          [ParameterVector.VECTOR_TYPE_ANY]))
        self.addParameter(ParameterSelection(self.TRANSF, 'Transformação',
                          self.TRANSF_OPTIONS))
        self.addParameter(ParameterSelection(self.CRS, 'Datum Antigo',
                          self.CRS_OPTIONS))
        self.addParameter(ParameterSelection(self.GRID, 'Grelha NTv2 a usar (Fonte)',
                          self.GRID_OPTIONS))
        self.addOutput(OutputVector(self.OUTPUT, 'Ficheiro de Saída'))

    def processAlgorithm(self, progress):
        inLayer = self.getParameterValue(self.INPUT)
        conn = self.ogrConnectionString(inLayer)

        output = self.getOutputFromName(self.OUTPUT)
        outFile = output.value

        if self.getParameterValue(self.TRANSF) == 0:
            # Transformacao Directa
            arguments = ['-s_srs']
            if self.getParameterValue(self.CRS) == 0:
                # Datum Lisboa
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=0 +y_0=0 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptLX_e89.gsb +wktext +pm=lisbon +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=0 +y_0=0 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/DLX_ETRS89_geo.gsb +wktext +pm=lisbon +units=m +no_defs')
            elif self.getParameterValue(self.CRS) == 1:
                # Datum Lisboa Militar
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=200000 +y_0=300000 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptLX_e89.gsb +wktext +pm=lisbon +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=200000 +y_0=300000 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/DLX_ETRS89_geo.gsb +wktext +pm=lisbon +units=m +no_defs')
            elif self.getParameterValue(self.CRS) == 2:
                # Datum 73
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=180.598 +y_0=-86.99 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/pt73_e89.gsb +wktext +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=180.598 +y_0=-86.99 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/D73_ETRS89_geo.gsb +wktext +units=m +no_defs')
            elif self.getParameterValue(self.CRS) == 3:
                # Datum 73 Militar
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=200180.598 +y_0=299913.01 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/pt73_e89.gsb +wktext +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=200180.598 +y_0=299913.01 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/D73_ETRS89_geo.gsb +wktext +units=m +no_defs')
            else:
                # ED50 UTM 29N - Jose Alberto Goncalves
                arguments.append('+proj=utm +zone=29 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptED_e89.gsb +wktext +units=m +no_defs')
            arguments.append('-t_srs')
            arguments.append('EPSG:3763')
        else:
            # Transformacao Inversa
            arguments = ['-s_srs']
            arguments.append('EPSG:3763')
            arguments.append('-t_srs')
            if self.getParameterValue(self.CRS) == 0:
                # Datum Lisboa
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=0 +y_0=0 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptLX_e89.gsb +wktext +pm=lisbon +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=0 +y_0=0 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/DLX_ETRS89_geo.gsb +wktext +pm=lisbon +units=m +no_defs')
            elif self.getParameterValue(self.CRS) == 1:
                # Datum Lisboa Militar
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=200000 +y_0=300000 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptLX_e89.gsb +wktext +pm=lisbon +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=200000 +y_0=300000 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/DLX_ETRS89_geo.gsb +wktext +pm=lisbon +units=m +no_defs')
            elif self.getParameterValue(self.CRS) == 2:
                # Datum 73
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=180.598 +y_0=-86.99 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/pt73_e89.gsb +wktext +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=180.598 +y_0=-86.99 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/D73_ETRS89_geo.gsb +wktext +units=m +no_defs')
            elif self.getParameterValue(self.CRS) == 3:
                # Datum 73 Militar
                if self.getParameterValue(self.GRID) == 0:
                    # Jose Alberto Goncalves
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=200180.598 +y_0=299913.01 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/pt73_e89.gsb +wktext +units=m +no_defs')
                else:
                    # Direccao Geral do Territorio
                    arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=200180.598 +y_0=299913.01 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/D73_ETRS89_geo.gsb +wktext +units=m +no_defs')
            else:
                # ED50 UTM 29N - Jose Alberto Goncalves
                arguments.append('+proj=utm +zone=29 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptED_e89.gsb +wktext +units=m +no_defs')
        arguments.append('-f')
        arguments.append('ESRI Shapefile')

        arguments.append(outFile)
        arguments.append(conn)

        commands = ['ogr2ogr', GdalUtils.escapeAndJoin(arguments)]
        GdalUtils.runGdal(commands, progress)
