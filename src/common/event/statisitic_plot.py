# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
import logging
import sys
import os

class statistic_plot_backend(object):
    """create a statistic of called testcases

    create a stat.dat file for creating a TC statistic image
    with gnuplot

    call "gnuplot balkenplot.sem" in tbot workdir after
    tbot finsihed, so you need gnuplot installed on your system.

    used balkenplot.sem file:

    https://github.com/hsdenx/tbot/blob/master/src/files/balkenplot.sem

    - **parameters**, **types**, **return** and **return types**::
    :param arg1: tb
    :param arg2: filename which gets created
    :param arg3: list of strings, containing testcasesnames, which get ignored
    """
    def __init__(self, tb, fdfile, ignorelist):
        self.dotnr = 0
        self.tb = tb
        self.ev = self.tb.event
        self.fdfile = fdfile
        self.fd = open(tb.workdir + '/' + fdfile, 'w')
        self.tc_list = []
        self.ignoretclist = ignorelist

    def _close(self):
        self.fd.close()

    def __del__(self):
        self._close()

    def create_statfile(self):
        """create the statistic file
        """
        el = list(self.tb.event.event_list)
        self._analyse(el)
        # self._print_list()
        self._write_header()
        self._write_table()
        self._write_bottom()
        self._close()
 
    def _write_header(self):
        self.fd.write('Name\tFail\tOk\n')
 
    def _write_bottom(self):
        self.fd.write('\n')

    def _get_event_typ(self, tmp):
        if tmp[self.ev.id] == 'Start':
            return tmp[self.ev.id]
        if tmp[self.ev.id] == 'StartFkt':
            return tmp[self.ev.id]
        if tmp[self.ev.id] == 'End':
            return tmp[self.ev.id]
        return 'none'

    def _get_event_name(self, tmp):
        return tmp[self.ev.name]

    def _get_next_event(self, el):
        if el == None:
            return ''

        if len(el) == 0:
            return ''

        ret = el[0]
        el.pop(0)
        return ret

    def _check_ignore_list(self, typ, name, evl):
        if not 'Start' in typ:
            return 'ok'

        for ign in self.ignoretclist:
            if ign == name:
                # search until End event
                line = 'start'
                while line != '':
                    line = self._get_next_event(evl)
                    tmp = line.split()
                    if tmp == []:
                        continue
                    if tmp[self.ev.typ] != 'EVENT':
                        continue
                    ntyp = self._get_event_typ(tmp)
                    if typ == 'none':
                        continue
                    newname = self._get_event_name(tmp)
                    if newname == name and ntyp == 'End':
                        return 'ignore'

        return 'ok'

    def _delete_in_list(self, val):
        self.tc_list.remove(val)

    def _search_in_list(self, name):
        for el in self.tc_list:
            if el[0] == name:
                return el

        return None

    def _add_to_list(self, name):
        newel = name, 0, 0
        self.tc_list.append(newel)

    def _print_list(self):
        print(self.tc_list)

    def _write_table(self):
        for el in self.tc_list:
            tmp = el[0] + '\t' + str(el[2]) + '\t' + str(el[1]) + '\n'
            self.fd.write(tmp)

    def _analyse(self, evl):
        line = 'start'
        while line != '':
            line = self._get_next_event(evl)
            tmp = line.split()
            if tmp == []:
                continue
            if tmp[self.ev.typ] != 'EVENT':
                continue
            typ = self._get_event_typ(tmp)
            if typ == 'none':
                continue
            newname = self._get_event_name(tmp)
            result = tmp[self.ev.value]
            ret = self._check_ignore_list(typ, newname, evl)
            if ret == 'ignore':
                continue
            if typ == 'Start' or typ == 'StartFkt':
                el = self._search_in_list(newname)
                if el == None:
                    self._add_to_list(newname)
            if typ == 'End':
                el = self._search_in_list(newname)
                if el == None:
                    print("Error End not found", newname)
                    continue
                if result == 'True':
                    new = el[1] + 1
                    newel = el[0], new, el[2]
                if result == 'False':
                    new = el[2] + 1
                    newel = el[0], el[1], new
                self._delete_in_list(el)
                self.tc_list.append(newel)
