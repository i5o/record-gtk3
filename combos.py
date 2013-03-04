#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       combos.py
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

from gettext import gettext as _
from IconCombo import IconComboBox

import hw


class TimerCombo(IconComboBox):
    TIMERS = (0, 5, 10)

    def __init__(self):
        super(TimerCombo, self).__init__('timer')

        for i in self.TIMERS:
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
    DURATIONS = (2, 4, 6)

    def __init__(self):
        super(DurationCombo, self).__init__('duration')

        for i in self.DURATIONS:
            string = str(i) + " " + _("minutes")
            self.append_item(i, string)
        self.combo.set_active(0)

    def get_value(self):
        return 60 * self.DURATIONS[self.combo.get_active()]

    def get_value_idx(self):
        return self.combo.get_active()

    def set_value_idx(self, idx):
        self.combo.set_active(idx)


class QualityCombo(Gtk.ComboBox):

    def __init__(self):
        super(QualityCombo, self).__init__()
        self._model = Gtk.ListStore(str)
        self._add(_("Low"))
        self.set_active(0)

        if hw.get_xo_version() != 1:
            self._add(_('High'))

        self.set_model(self._model)
        self.show_all()

    def _add(self, text):
        self._render = Gtk.CellRendererText()
        self._model.append([text])
        self.pack_start(self._render, True)
        self.add_attribute(self._render, "text", 0)
