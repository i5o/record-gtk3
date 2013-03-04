#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       utils.py
#
#       Copyright (C) 2013 Ignacio Rodríguez <ignacio@sugarlabs.org>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from gi.repository import GConf
from sugar3.graphics.xocolor import XoColor
from sugar3.graphics.icon import Icon

CLIENT = GConf.Client.get_default()


def _get_xo_color():
    info = CLIENT.get_string("/desktop/sugar/user/color")
    color = XoColor(info)
    return color


def _get_icon_with_color(icon_name, size):
    color = _get_xo_color()
    return Icon(xo_color=color, icon_name=icon_name, pixel_size=size)