#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Widgets.py por:

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

from gettext import gettext as _

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject

import sugar3
from sugar3.graphics.combobox import ComboBox
from sugar3.graphics import style
from sugar3.graphics.icon import Icon

class IconComboBox(Gtk.ToolItem):
    
    def __init__(self, icon_name):
        
        Gtk.ToolItem.__init__(self)

        self.icon_name = icon_name
        self.set_border_width(style.DEFAULT_PADDING)

        self.combo = ComboBox()
        self.combo.set_focus_on_click(False)
        self.combo.show()

        self.add(self.combo)

    def append_item(self, i, text):
        
        self.combo.append_item(i, text, icon_name=self.icon_name)
        
class TimerCombo(IconComboBox):

    def __init__(self):
        
        super(TimerCombo, self).__init__('timer')

        for i in [0, 5, 10]:
            if i == 0:
                self.append_item(i, _('Immediate'))
                
            else:
                string = str(i) + " " + _("seconds")
                self.append_item(i, string)
                
        self.combo.set_active(0)

    def get_value(self):
        
        return TimerCombo.TIMERS[self.combo.get_active()]

    def get_value_idx(self):
        
        return self.combo.get_active()

    def set_value_idx(self, idx):
        
        self.combo.set_active(idx)

class DurationCombo(IconComboBox):

    def __init__(self):
        
        super(DurationCombo, self).__init__('duration')

        for i in [2, 4, 6]:
            string = str(i) + " " + _("minutes")
            self.append_item(i, string)
            
        self.combo.set_active(0)

    def get_value(self):
        
        #return 60 * self.DURATIONS[self.combo.get_active()]
        pass

    def get_value_idx(self):
        
        return self.combo.get_active()

    def set_value_idx(self, idx):
        
        self.combo.set_active(idx)

class QualityCombo(Gtk.ComboBox):

    def __init__(self):
        
        super(QualityCombo, self).__init__()
        
        self._model = Gtk.ListStore(str)

        self._render = Gtk.CellRendererText()
        self.pack_start(self._render, True)
        self.add_attribute(self._render, "text", 0)

        self._add(_("Low"))
        self._add(_('High'))

        self.set_active(0)
        
        self.set_model(self._model)
        self.show_all()

    def _add(self, text):
        
        self._model.append([text])
        
class View(Gtk.DrawingArea):
    
    __gtype_name__ = 'Visor'
    
    def __init__(self):
        
        Gtk.DrawingArea.__init__(self)
        
        self.add_events(
            Gdk.EventMask.KEY_PRESS_MASK |
            Gdk.EventMask.KEY_RELEASE_MASK |
            Gdk.EventMask.POINTER_MOTION_MASK |
            Gdk.EventMask.POINTER_MOTION_HINT_MASK |
            Gdk.EventMask.BUTTON_MOTION_MASK |
            Gdk.EventMask.BUTTON_PRESS_MASK |
            Gdk.EventMask.BUTTON_RELEASE_MASK
        )
        
        self.show_all()
        
class Tray(Gtk.Box):
    
    def __init__(self):
        
        Gtk.Box.__init__(self, orientation = Gtk.Orientation.HORIZONTAL)
        
        self.set_size_request(-1, 150)
        
        scroll_left = TrayScrollButton('go-left')
        self.pack_start(scroll_left, False, False, 0)

        '''
        scroll = Gtk.ScrolledWindow()
        
        scroll.set_policy(
            Gtk.PolicyType.AUTOMATIC,
            Gtk.PolicyType.NEVER)'''
        
        toolbar = Gtk.Toolbar(orientation = Gtk.Orientation.HORIZONTAL)
        toolbar.set_show_arrow(False)
        toolbar.set_size_request(500, -1)
        toolbar.show()
        
        scroll = Gtk.Viewport()
        scroll.set_shadow_type(Gtk.ShadowType.NONE)
        
        scroll.add(toolbar)
        #scroll.add_with_viewport(toolbar)
        
        self.pack_start(scroll, True, False, 0)
        
        scroll_right = TrayScrollButton('go-right')
        self.pack_end(scroll_right, False, False, 0)
        
        self.show_all()
        
class TrayScrollButton(Gtk.Button):
    
    def __init__(self, icon_name):
        
        Gtk.Button.__init__(self)
        
        self.modify_bg(
            Gtk.StateType.NORMAL,
            style.COLOR_TOOLBAR_GREY.get_gdk_color())
            
        self.modify_bg(
            Gtk.StateType.ACTIVE,
            style.COLOR_BUTTON_GREY.get_gdk_color())
            
        self.set_relief(Gtk.ReliefStyle.NONE)
        
        self.set_size_request(
            style.GRID_CELL_SIZE,
            style.GRID_CELL_SIZE)

        icon = Icon(
            icon_name = icon_name,
            icon_size = Gtk.IconSize.SMALL_TOOLBAR)
            
        self.set_image(icon)
        
        icon.show()
        
        self.show_all()
        
        #self.connect('clicked', self._clicked_cb)
        