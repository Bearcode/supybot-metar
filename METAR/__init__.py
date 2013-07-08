###
#
# METAR/plugin.py: METAR information plugin for supybot, initialization
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

"""
Displays METAR information for specified ICAO code.
"""

import supybot
import supybot.world as world

# Plugin information stuff
__version__ = "0.1"
__author__ = supybot.Author('Daniil Baturin', 'dmbaturin',
                            'daniil at baturin dot org')
__contributors__ = {}
__url__ = 'https://github.com/dmbaturin/supybot-metar'

from . import config
from . import plugin
from imp import reload
import re
import urllib2

# In case we're being reloaded.
reload(config)
reload(plugin)
reload(re)
reload(urllib2)
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
