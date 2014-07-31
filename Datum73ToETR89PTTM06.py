# -*- coding: utf-8 -*-

"""
***************************************************************************
    Datum73ToETR89PTTM06.py
    ---------------------
    Date                 : July 2014
    Copyright            : (C) 2014 by Alexander Bruy
    Email                : alexander dot bruy at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alexander Bruy'
__date__ = 'July 2014'
__copyright__ = '(C) 2014, Alexander Bruy'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from PyQt4.QtCore import *
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


class Datum73ToETR89PTTM06(OgrAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    GRID = 'GRELHAS'
    GRID_OPTIONS = ['JAG', 'DGT']

    def defineCharacteristics(self):
        self.name = 'From Datum 73 to ETRS89-PTTM06'
        self.group = 'Vector Datum Transformations'

        self.addParameter(ParameterVector(self.INPUT, 'Input layer',
                          [ParameterVector.VECTOR_TYPE_ANY]))
        self.addParameter(ParameterSelection(self.GRID, 'Grelhas a Usar (JAG - Jose Alberto Goncalves; DGT - Direccao Geral do Territorio)',
                          self.GRID_OPTIONS))
        self.addOutput(OutputVector(self.OUTPUT, 'Output layer'))

    def processAlgorithm(self, progress):
        inLayer = self.getParameterValue(self.INPUT)
        conn = self.ogrConnectionString(inLayer)

        output = self.getOutputFromName(self.OUTPUT)
        outFile = output.value

        arguments = []
        if self.GRID_OPTIONS[self.getParameterValue(self.GRID)] == 'JAG':
            arguments.append('-s_srs')
            arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=180.598 +y_0=-86.99 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/pt73_e89.gsb +wktext +units=m +no_defs')
        else:
            arguments.append('-s_srs')
            arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=-8.131906111111112 +k=1 +x_0=180.598 +y_0=-86.99 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/D73_ETRS89_geo.gsb +wktext +units=m +no_defs')
        arguments.append('-t_srs')
        arguments.append('EPSG:3763')
        arguments.append('-f')
        arguments.append('ESRI Shapefile')

        arguments.append(outFile)
        arguments.append(conn)

        commands = ['ogr2ogr', GdalUtils.escapeAndJoin(arguments)]
        GdalUtils.runGdal(commands, progress)
