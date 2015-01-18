###
#
# METAR/plugin.py: METAR information plugin for supybot
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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('METAR')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

import urllib3
import re


METAR_URL = "http://weather.noaa.gov/pub/data/observations/metar/decoded/%s.TXT"
RAW_METAR_URL = "http://weather.noaa.gov/pub/data/observations/metar/stations/%s.TXT"


class METAR(callbacks.Plugin):
    """Add the help for "@plugin help METAR" here
    This should describe *how* to use this plugin."""
    threaded = True

    def __init__(self, irc):
        self.__parent = super(METAR, self)
        self.__parent.__init__(irc)
        self._http = urllib3.PoolManager()
        self._station_regex = re.compile("^[a-zA-Z]{4}$")

    def _valid_station_code(self, station):
        if not self._station_regex.match(station):
            return False
        else:
            return True

    def imetar(self, irc, msg, args, station):
        """[<ICAO airport code>]

        Shows METAR information for <ICAO airport code>.
        """

        if not self._valid_station_code(station):
            irc.reply(station + " can't be a valid ICAO code")
            return 1

        try:
            station = station.upper()
            url = METAR_URL % station
            reply = self._http.request('GET', url)
        except Exception as e:
            irc.reply("Could not fetch report for " + station + ". Make sure your code is correct and try again later.")
            return 1

        report_lines = reply.data.split("\n")
        for line in report_lines:
            if line: 
                irc.reply(line, to=msg.nick, prefixNick=False,
                          private=True)

    imetar = wrap(imetar, ['something'])

    def metar(self, irc, msg, args, station):
        """<ICAO airport code>
        
           Display raw METAR information for <ICAO airport code>
        """

        if not self._valid_station_code(station):
            irc.reply(station + " can't be a valid ICAO code")
            return 1

        try:
            station = station.upper()
            url = RAW_METAR_URL % station
            url = METAR_URL % station
            reply = self._http.request('GET', url)
        except Exception as e:
            irc.reply("Could not fetch report for " + station + ". Make sure your code is correct and try again later.")
            return 1

        result = " ".join( reply.data.split("\n") )
        irc.reply(result)

    metar = wrap(metar, ["something"])


Class = METAR


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
