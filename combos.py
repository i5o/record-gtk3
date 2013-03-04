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

from gettext import gettext as _
from IconCombo import IconComboBox

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
