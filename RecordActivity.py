#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   RecordActivity.py por:

#   Ignacio Rodríguez <ignacio@sugarlabs.org>
#   Flavio Danesse <fdanesse@gmail.com>
#   CeibalJAM! - pyhon_joven - Uruguay

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os

from gettext import gettext as _

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject

from sugar3.graphics.radiotoolbutton import RadioToolButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolcombobox import ToolComboBox
from sugar3.activity import activity

from Widgets import DurationCombo
from Widgets import TimerCombo
from Widgets import QualityCombo
from Widgets import View
from Widgets import Tray

BASE = os.path.dirname(__file__)

screen = Gdk.Screen.get_default()
css_provider = Gtk.CssProvider()
style_path = os.path.join(BASE, "RecordStyle.css")
css_provider.load_from_path(style_path)
context = Gtk.StyleContext()

context.add_provider_for_screen(
    screen,
    css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_USER)
    
class Record(activity.Activity):
    
    def __init__(self, handle):
        
        super(Record, self).__init__(handle)

        self.toolbox = ToolbarBox()
        self.toolbar = self.toolbox.toolbar
        self.activitybutton = ActivityToolbarButton(self)
        
        self._photo = None
        self._video = None
        self._audio = None
        
        self._timer = None
        self._timer_2 = None
        
        self._preferencias = None
        
        self.view = None
        self.tray = None
        
        self._set_toolbar()
        self._set_canvas()
        
        self.show_all()
        
        #self._photo.connect("clicked", self._click, "Photo")
        #self._video.connect("clicked", self._click, "Video")
        #self._audio.connect("clicked", self._click, "Audio")

    def _set_canvas(self):
        
        basebox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        
        self.view = View()
        self.tray = Tray()
        
        basebox.pack_start(self.view, True, True, 0)
        basebox.pack_start(self.tray, False, False, 0)
        
        self.set_canvas(basebox)
        
    def _set_toolbar(self):
        
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
        #self._timer_2.combo.set_sensitive(False)

        self._preferencias = ToolbarButton()
        
        toolbar = Gtk.Toolbar()
        combo = QualityCombo()
        #combo.set_sensitive(False)
        self.calidad = ToolComboBox(combo=combo, label_text=_('Quality:'))
        self.calidad.show_all()
        toolbar.insert(self.calidad, -1)
        toolbar.show_all()
        
        self._preferencias.set_page(toolbar)
        
        self._preferencias.props.icon_name = 'preferences-system'
        self._preferencias.props.label = _('Preferences')

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
        
    '''
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
            self.calidad.combo.set_sensitive(False)'''
