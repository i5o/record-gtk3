#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       IconCombo.py
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

from gi.repository import Gtk
from sugar3.graphics.combobox import ComboBox
from sugar3.graphics import style

class IconComboBox(Gtk.ToolItem):
    def __init__(self, icon_name, **kwargs):
        Gtk.ToolItem.__init__(self, **kwargs)

        self.icon_name = icon_name
        self.set_border_width(style.DEFAULT_PADDING)

        self.combo = ComboBox()
        self.combo.set_focus_on_click(False)
        self.combo.show()

        self.add(self.combo)

    def append_item(self, i, text):
        self.combo.append_item(i, text, icon_name=self.icon_name)
