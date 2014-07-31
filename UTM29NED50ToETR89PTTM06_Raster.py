# -*- coding: utf-8 -*-

"""
***************************************************************************
    UTM29NED50ToETR89PTTM06_Raster.py
    ---------------------
    Date                 : July 2014
    Copyright            : (C) 2014 by Pedro Venâncio, Giovanni Manghi
    Email                : pedrongvenancio at yahoo dot com
                           giovanni dot manghi at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Pedro Venâncio, Giovanni Manghi'
__date__ = 'July 2014'
__copyright__ = '(C) 2014, Pedro Venâncio, Giovanni Manghi'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from qgis.core import *

try:
    from processing.parameters.ParameterRaster import ParameterRaster
    from processing.outputs.OutputRaster import OutputRaster
except:
    from processing.core.parameters import ParameterRaster
    from processing.core.outputs import OutputRaster

from processing.algs.gdal.GdalAlgorithm import GdalAlgorithm
from processing.algs.gdal.GdalUtils import GdalUtils


class UTM29NED50ToETR89PTTM06_Raster(GdalAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def defineCharacteristics(self):
        self.name = 'From UTM 29N ED50 to ETR89-PTTM06 Raster'
        self.group = 'Raster Datum Transformations'
        self.addParameter(ParameterRaster(self.INPUT, 'Input layer', False))
        self.addOutput(OutputRaster(self.OUTPUT, 'Output layer'))

    def processAlgorithm(self, progress):
        arguments = ['-s_srs',
                     '+proj=utm +zone=29 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptED_e89.gsb +wktext +units=m +no_defs',
                     '-t_srs',
                     'EPSG:3763',
                     '-r',
                     'bilinear',
                     '-dstnodata',
                     'nan'
                    ]
        arguments.append('-of')
        out = self.getOutputValue(self.OUTPUT)
        arguments.append(GdalUtils.getFormatShortNameFromFilename(out))
        arguments.append(self.getParameterValue(self.INPUT))
        arguments.append(out)

        GdalUtils.runGdal(['gdalwarp', GdalUtils.escapeAndJoin(arguments)],
                          progress)
