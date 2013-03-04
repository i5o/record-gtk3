#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       RecordActivity.py
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

from sugar3.graphics.radiotoolbutton import RadioToolButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton

from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolcombobox import ToolComboBox

from sugar3.graphics.combobox import ComboBox

from sugar3.activity import activity

from gettext import gettext as _

from combos import DurationCombo
from combos import TimerCombo
from combos import QualityCombo



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
        
        # Buttons #
        self._photo = RadioToolButton()
        self._photo.props.icon_name = 'media-photo'
        self._photo.props.label = _('Photo')

        self._video = RadioToolButton()
        self._video.props.group = self._photo
        self._video.props.icon_name = 'media-video'
        self._video.props.label = _('Video')

        self._audio = RadioToolButton()
        self._audio.props.group = self._photo
        self._audio.props.icon_name = 'media-audio'
        self._audio.props.label = _('Audio')
        # End of Buttons #

        self._timer = TimerCombo()
        self._timer_2 = DurationCombo()
        self._timer_2.combo.set_sensitive(False)

        self._preferencias = ToolbarButton()
        self._preferencias.set_page(self._make_config_toolbar())
        self._preferencias.props.icon_name = 'preferences-system'
        self._preferencias.props.label = _('Preferences')


        self._photo.connect("clicked", self._click, "Photo")
        self._video.connect("clicked", self._click, "Video")
        self._audio.connect("clicked", self._click, "Audio")

        self.toolbar.insert(self.activitybutton, -1)

        self.toolbar.insert(self._photo, -1)
        self.toolbar.insert(self._video, -1)
        self.toolbar.insert(self._audio, -1)

        self.toolbar.insert(Gtk.SeparatorToolItem(), -1)

        self.toolbar.insert(self._timer, -1)
        self.toolbar.insert(self._timer_2, -1)
        self.toolbar.insert(self._preferencias, -1)

        self.toolbar.insert(separator, -1)
        self.toolbar.insert(stop, -1)

        self.set_toolbar_box(self.toolbox)
        self.show_all()


    def _click(self, widget, mode):       
        for widget in self._timer_2:
            if mode == "Video" or mode == "Audio":
                widget.set_sensitive(True)
            else:
                widget.set_sensitive(False)
            widget.show_all()

        if mode == "Video":
            self.calidad.combo.set_sensitive(True)
        else:
            self.calidad.combo.set_sensitive(False)

    def _make_config_toolbar(self):
        toolbar = Gtk.Toolbar()
        combo = QualityCombo()
        combo.set_sensitive(False)
        self.calidad = ToolComboBox(combo=combo, label_text=_('Quality:'))
        self.calidad.show_all()
        
        toolbar.insert(self.calidad, -1)
        toolbar.show_all()
        return toolbar       

