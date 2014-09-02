# -*- coding: latin-1 -*-

"""
***************************************************************************
    DatumLisboaToETR89PTTM06_Raster.py
    ---------------------
    Date                 : July 2014
    Copyright            : (C) 2014 by Pedro Venâncio, Giovanni Manghi
    Email                : pedrongvenancio at gmail dot com
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

from PyQt4.QtGui import *

from qgis.core import *

try:
    from processing.parameters.ParameterRaster import ParameterRaster
    from processing.parameters.ParameterSelection import ParameterSelection
    from processing.outputs.OutputRaster import OutputRaster
except:
    from processing.core.parameters import ParameterRaster
    from processing.core.parameters import ParameterSelection
    from processing.core.outputs import OutputRaster

from processing.algs.gdal.GdalAlgorithm import GdalAlgorithm
from processing.algs.gdal.GdalUtils import GdalUtils


class DatumLisboaToETR89PTTM06_Raster(GdalAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    GRID = 'GRELHAS'
    GRID_OPTIONS = ['José Alberto Gonçalves',
                    'Direção-Geral do Territorio']

    def getIcon(self):
        return  QIcon(os.path.dirname(__file__) + '/icons/pttransform.svg')

    def defineCharacteristics(self):
        self.name = 'De Datum Lisboa para PT-TM06/ETRS89 Raster'
        self.group = 'Transformação de Datum em Rasters'
        self.addParameter(ParameterRaster(self.INPUT, 'Ficheiro de Entrada', False))
        self.addParameter(ParameterSelection(self.GRID, 'Grelha NTv2 a usar (Fonte)',
                          self.GRID_OPTIONS))
        self.addOutput(OutputRaster(self.OUTPUT, 'Ficheiro de Saída'))

    def processAlgorithm(self, progress):
        arguments = ['-s_srs']
        if self.getParameterValue(self.GRID) == 0:
            # Jose Alberto Goncalves
            arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=0 +y_0=0 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptLX_e89.gsb +wktext +pm=lisbon +units=m +no_defs')
        else:
            # Direccao Geral do Territorio
            arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=0 +y_0=0 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/DLX_ETRS89_geo.gsb +wktext +pm=lisbon +units=m +no_defs')
        arguments.append('-t_srs')
        arguments.append('EPSG:3763')
        arguments.append('-r')
        arguments.append('bilinear')
        arguments.append('-dstnodata')
        arguments.append('nan')
        arguments.append('-of')
        out = self.getOutputValue(self.OUTPUT)
        arguments.append(GdalUtils.getFormatShortNameFromFilename(out))
        arguments.append(self.getParameterValue(self.INPUT))
        arguments.append(out)

        GdalUtils.runGdal(['gdalwarp', GdalUtils.escapeAndJoin(arguments)],
                          progress)
