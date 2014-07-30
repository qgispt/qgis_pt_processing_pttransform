# -*- coding: utf-8 -*-

"""
***************************************************************************
    DatumLisboaMilToETR89PTTM06_Raster.py
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
from processing.algs.gdal.GdalAlgorithm import GdalAlgorithm
from processing.parameters.ParameterRaster import ParameterRaster
from processing.parameters.ParameterSelection import ParameterSelection
from processing.parameters.ParameterCrs import ParameterCrs
from processing.parameters.ParameterNumber import ParameterNumber
from processing.parameters.ParameterString import ParameterString
from processing.outputs.OutputRaster import OutputRaster
from processing.algs.gdal.GdalUtils import GdalUtils


class DatumLisboaMilToETR89PTTM06_Raster(GdalAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    GRID = 'GRELHAS'
    GRID_OPTIONS = ['JAG', 'DGT']

    def defineCharacteristics(self):
        self.name = 'From Datum Lisboa Militar to ETRS89-PTTM06 Raster'
        self.group = 'Raster Datum Transformations'
        self.addParameter(ParameterRaster(self.INPUT, 'Input layer', False))
        self.addParameter(ParameterSelection(self.GRID, 'Grelhas a Usar (JAG - Jose Alberto Goncalves; DGT - Direccao Geral do Territorio)',
                          self.GRID_OPTIONS))
        self.addOutput(OutputRaster(self.OUTPUT, 'Output layer'))


    def processAlgorithm(self, progress):
        arguments = []
        if self.GRID_OPTIONS[self.getParameterValue(self.GRID)] == 'JAG':
            arguments.append('-s_srs')
            arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=200000 +y_0=300000 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/ptLX_e89.gsb +wktext +pm=lisbon +units=m +no_defs')
        else:
            arguments.append('-s_srs')
            arguments.append('+proj=tmerc +lat_0=39.66666666666666 +lon_0=1 +k=1 +x_0=200000 +y_0=300000 +ellps=intl +nadgrids=' + os.path.dirname(__file__) + '/grids/DLX_ETRS89_geo.gsb +wktext +pm=lisbon +units=m +no_defs')
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
