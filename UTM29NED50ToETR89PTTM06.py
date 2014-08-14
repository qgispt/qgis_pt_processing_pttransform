# -*- coding: latin-1 -*-

"""
***************************************************************************
    UTM29NED50ToETR89PTTM06.py
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

from PyQt4.QtGui import *

from qgis.core import *

try:
    from processing.parameters.ParameterVector import ParameterVector
    from processing.outputs.OutputVector import OutputVector
except:
    from processing.core.parameters import ParameterVector
    from processing.core.outputs import OutputVector

from processing.algs.gdal.OgrAlgorithm import OgrAlgorithm
from processing.algs.gdal.GdalUtils import GdalUtils

from processing.tools.system import *

class UTM29NED50ToETR89PTTM06(OgrAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def getIcon(self):
        return  QIcon(os.path.dirname(__file__) + '/icons/pttransform.svg')

    def defineCharacteristics(self):
        self.name = 'De UTM 29N ED50 para PT-TM06/ETRS89'
        self.group = 'Transformações de Datum em Vectores'

        self.addParameter(ParameterVector(self.INPUT, 'Ficheiro de Entrada',
                          [ParameterVector.VECTOR_TYPE_ANY]))
        self.addOutput(OutputVector(self.OUTPUT, 'Ficheiro de Saída'))

    def processAlgorithm(self, progress):
        inLayer = self.getParameterValue(self.INPUT)
        conn = self.ogrConnectionString(inLayer)

        output = self.getOutputFromName(self.OUTPUT)
        outFile = output.value

        arguments = ['-f',
                     'ESRI Shapefile',
                     '-s_srs',
                     '+proj=utm +zone=29 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptED_e89.gsb +wktext +units=m +no_defs',
                     '-t_srs',
                     'EPSG:3763',
                     outFile,
                     conn
                    ]

        commands = ['ogr2ogr', GdalUtils.escapeAndJoin(arguments)]
        GdalUtils.runGdal(commands, progress)
