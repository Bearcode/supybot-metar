###
#
# METAR/test.py: METAR information plugin for supybot, tests
#
# Copyright (C) 2013 Daniil Baturin <daniil at baturin dot org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
###

from supybot.test import *

class METARTestCase(PluginTestCase):
    plugins = ('METAR',)


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
