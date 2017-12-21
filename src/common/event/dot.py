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

class dot(object):
    """create a dot description file from the executed testcases.

    after tbot hs finsihed create a png with:
      dot -Tpng tc.dot > tc.png
    or create a postscript with:
      dot -Tps tc.dot > tc.ps

    - **parameters**, **types**, **return** and **return types**::
    :param arg1: tb
    :param arg2: filename, which contains the dot description data
    :param arg3: list of strings, containing testcasesnames, which get ignored
    """
    def __init__(self, tb, dotfile, ignorelist):
        self.tb = tb
        self.ev = self.tb.event
        self.dotfile = dotfile
        self.fd = open(self.tb.workdir + '/' + self.dotfile, 'w')
        self.dotnr = 0
        self.ignoretclist = ignorelist

    def create_dotfile(self):
        """create the dot file
        """
        self._write_header()
        self._write_table()
        self._write_bottom()
        self.fd.close()
        os.system("dot -Tpng " + self.tb.workdir + "/tc.dot > " + self.tb.workdir + "/tc.png")
 
    def _write_header(self):
        self.fd.write('digraph tc_dot_output\n{\nrankdir=LR;\n')
 
    def _write_bottom(self):
        self.fd.write('}\n')

    def _create_knoten(self, name, col='black'):
        self.dotnr = self.dotnr + 1
        nr = self.dotnr
        tmp = str(nr) + ' [shape=record, label="' + name + '" color=' + col+ '];\n'
        self.fd.write(tmp)
        return nr

    def _write_knotenline(self, last, new, color):
        tmp = str(last) + ' ->  ' + str(new) + ' [color=' + color +']\n'
        self.fd.write(tmp)

    def _get_event_id(self, el):
        if el['id'] == 'Start':
            return el['id']
        if el['id'] == 'StartFkt':
            return el['id']
        if el['id'] == 'End':
            return el['id']
        return 'none'

    def _get_event_name(self, el):
        return el['fname']

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
                el = 'start'
                while el != '':
                    el = self._get_next_event(evl)
                    if el == '':
                        continue
                    if el['typ'] != 'EVENT':
                        continue
                    ntyp = self._get_event_id(el)
                    if ntyp == 'none':
                        continue
                    newname = self._get_event_name(el)
                    if newname == name and ntyp == 'End':
                        return 'ignore'

        return 'ok'

    def _call_anal(self, name, current, evl):
        el = 'start'
        while el != '':
            el = self._get_next_event(evl)
            if el == '':
                continue
            if el['typ'] != 'EVENT':
                continue
            typ = self._get_event_id(el)
            if typ == 'none':
                continue
            newname = self._get_event_name(el)
            result = el['val']
            ret = self._check_ignore_list(typ, newname, evl)
            if ret == 'ignore':
                continue
            if typ == 'Start':
                nr = self._create_knoten(newname)
                self._write_knotenline(current, nr, 'black')
                color = self._call_anal(newname, nr, evl)
                self._write_knotenline(nr, current, color)

            if typ == 'StartFkt':
                nr = self._create_knoten(newname, col='blue')
                self._write_knotenline(current, nr, 'blue')
                color = self._call_anal(newname, nr, evl)
                self._write_knotenline(nr, current, color)

            if typ == 'End':
                if result == 'True':
                    color = 'green'
                else:
                    color = 'red'
                return color
        return 'end'
    
    def _write_table(self):
        evl = list(self.tb.event.event_list)
        nr = self._create_knoten('main')
        end = 'go'
        while end != 'end':
            end = self._call_anal('main', nr, evl)
