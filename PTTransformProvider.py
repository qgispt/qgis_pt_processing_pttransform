# -*- coding: latin-1 -*-

"""
***************************************************************************
    CircuitscapeProvider.py
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

from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from processing.tools import system

from processing_pttransform.Datum73ToETR89PTTM06 import Datum73ToETR89PTTM06
from processing_pttransform.Datum73MilToETR89PTTM06 import Datum73MilToETR89PTTM06
from processing_pttransform.DatumLisboaToETR89PTTM06 import DatumLisboaToETR89PTTM06
from processing_pttransform.DatumLisboaMilToETR89PTTM06 import DatumLisboaMilToETR89PTTM06
from processing_pttransform.DatumLisboaMilToETR89PTTM06_Raster import DatumLisboaMilToETR89PTTM06_Raster
from processing_pttransform.DatumLisboaToETR89PTTM06_Raster import DatumLisboaToETR89PTTM06_Raster
from processing_pttransform.Datum73ToETR89PTTM06_Raster import Datum73ToETR89PTTM06_Raster
from processing_pttransform.Datum73MilToETR89PTTM06_Raster import Datum73MilToETR89PTTM06_Raster
from processing_pttransform.UTM29NED50ToETR89PTTM06_Raster import UTM29NED50ToETR89PTTM06_Raster
from processing_pttransform.UTM29NED50ToETR89PTTM06 import UTM29NED50ToETR89PTTM06


class PTTransformProvider(AlgorithmProvider):

    def __init__(self):
        AlgorithmProvider.__init__(self)

        self.activate = False

        self.alglist = [Datum73ToETR89PTTM06(),
                        Datum73MilToETR89PTTM06(),
                        DatumLisboaToETR89PTTM06(),
                        DatumLisboaMilToETR89PTTM06(),
                        DatumLisboaMilToETR89PTTM06_Raster(),
                        DatumLisboaToETR89PTTM06_Raster(),
                        Datum73ToETR89PTTM06_Raster(),
                        Datum73MilToETR89PTTM06_Raster(),
                        UTM29NED50ToETR89PTTM06_Raster(),
                        UTM29NED50ToETR89PTTM06()
                       ]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)

    def unload(self):
        AlgorithmProvider.unload(self)

    def getName(self):
        return 'Transformações de Datum para Portugal'

    def getDescription(self):
        return 'Transformações de Datum para Portugal'

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + '/icons/pttransform.svg')

    def _loadAlgorithms(self):
        self.algs = self.alglist
