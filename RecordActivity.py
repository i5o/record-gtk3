#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       activity.py
#
#       Copyright (C) 2013 Ignacio Rodríguez <ignacio@sugarlabs.org>
#       Copyright (C) 2013 Flavio Danesse <fdanesse@activitycentral.com>
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
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton
from gettext import gettext as _
from sugar3.activity import activity


class Record(activity.Activity):
    def __init__(self, handle):
        super(Record, self).__init__(handle)

        self.toolbox = ToolbarBox()
        self.toolbar = self.toolbox.toolbar

        self.activitybutton = ActivityToolbarButton(self)

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)

        stop = StopButton(self)


        self.toolbar.insert(self.activitybutton, -1)
        self.toolbar.insert(Gtk.SeparatorToolItem(), -1)
        self.toolbar.insert(separator, -1)
        self.toolbar.insert(stop, -1)

        self.set_toolbar_box(self.toolbox)
        self.show_all()
