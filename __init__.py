# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MINDED_FBA
                                 A QGIS plugin
 A non-supervised remote sensing tool for the determination of both flooded or burned extents.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-10-18
        copyright            : (C) 2022 by Oliveira et al., 2022
        email                : eduardo.oliveira@ua.pt
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MINDED_FBA class from file MINDED_FBA.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .MINDED_FBA import MINDED_FBA
    return MINDED_FBA(iface)