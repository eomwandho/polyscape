# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolyScape
                                 A QGIS plugin
 A tool forpolicy  decision making
                             -------------------
        begin                : 2014-02-12
        copyright            : (C) 2014 by ICRAF/ Univeristy of Bogor
        email                : e.omwandho@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load PolyScape class from file PolyScape
    from polyscape import PolyScape
    return PolyScape(iface)
