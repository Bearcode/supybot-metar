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

import pymetar

RAW_METAR_URL = "http://weather.noaa.gov/pub/data/observations/metar/stations/"

class METAR(callbacks.Plugin):
    """Add the help for "@plugin help METAR" here
    This should describe *how* to use this plugin."""
    threaded = True

    def __init__(self, irc):
        self.__parent = super(METAR, self)
        self.__parent.__init__(irc)

    def imetar(self, irc, msg, args, station):
        """[<ICAO airport code>]

        Shows METAR information for <ICAO airport code>.
        """
        try:
            fetcher = pymetar.ReportFetcher(station)
            report = fetcher.FetchReport()
        except Exception, e:
            irc.reply("Could not fetch report for " + station + ". Try again later.")
            irc.reply(str(e))
            return 1

        report_lines = report.fullreport.split("\n")
        for line in report_lines:
            if line: 
                irc.reply(line, to=msg.nick, prefixNick=False,
                          private=True)

    imetar = wrap(imetar, ['something'])

    def metar(self, irc, msg, args, station):
        """<ICAO airport code>
        
           Display raw METAR information for <ICAO airport code>
        """
        try:
            fetcher = pymetar.ReportFetcher(station, RAW_METAR_URL)
            report = fetcher.FetchReport()
        except Exception, e:
            irc.reply("Could not fetch report for " + station + ". Try again later.")
            irc.reply(str(e))
            return 1

        result = " ".join( report.fullreport.split("\n") )
        irc.reply(result)

    metar = wrap(metar, ["something"])


Class = METAR


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
