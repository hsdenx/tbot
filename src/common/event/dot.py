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
    def __init__(self, tb, dotfile, ignorelist):
        """
        create a dot description file from the executed testcases.
        after tbot hs finsihed
        create a png with:
          dot -Tpng tc.dot > tc.png
        or create a postscript with:
          dot -Tps tc.dot > tc.ps
        """
        self.tb = tb
        self.ev = self.tb.event
        self.dotfile = dotfile
        self.fd = open(self.tb.workdir + '/' + self.dotfile, 'w')
        self.dotnr = 0
        self.ignoretclist = ignorelist

    def create_dotfile(self):
        self.write_header()
        self.write_table()
        self.write_bottom()
        self.fd.close()
 
    def write_header(self):
        self.fd.write('digraph tc_dot_output\n{\nrankdir=LR;\n')
 
    def write_bottom(self):
        self.fd.write('}\n')

    def create_knoten(self, name):
        self.dotnr = self.dotnr + 1
        nr = self.dotnr
        tmp = str(nr) + ' [shape=record, label="' + name + '"];\n'
        self.fd.write(tmp)
        return nr

    def write_knotenline(self, last, new, color):
        tmp = str(last) + ' ->  ' + str(new) + ' [color=' + color +']\n'
        self.fd.write(tmp)

    def get_event_typ(self, tmp):
        if tmp[self.ev.id] == 'Start':
            return tmp[self.ev.id]
        if tmp[self.ev.id] == 'End':
            return tmp[self.ev.id]
        return 'none'

    def get_event_name(self, tmp):
        return tmp[self.ev.name]

    def get_next_event(self, el):
        if len(el) == 0:
            return ''

        ret = el[0]
        el.pop(0)
        return ret

    def check_ignore_list(self, typ, name, el):
        if typ != 'Start':
            return 'ok'

        for ign in self.ignoretclist:
            if ign == name:
                # search until End event
                line = 'start'
                while line != '':
                    line = self.get_next_event(el)
                    tmp = line.split()
                    if tmp == []:
                        continue
                    if tmp[self.ev.typ] != 'EVENT':
                        continue
                    ntyp = self.get_event_typ(tmp)
                    if typ == 'none':
                        continue
                    newname = self.get_event_name(tmp)
                    if newname == name and ntyp == 'End':
                        return 'ignore'

        return 'ok'

    def call_anal(self, name, current, el):
        line = 'start'
        while line != '':
            line = self.get_next_event(el)
            tmp = line.split()
            if tmp == []:
                continue
            if tmp[self.ev.typ] != 'EVENT':
                continue
            typ = self.get_event_typ(tmp)
            if typ == 'none':
                continue
            newname = self.get_event_name(tmp)
            result = tmp[self.ev.value]
            ret = self.check_ignore_list(typ, newname, el)
            if ret == 'ignore':
                continue
            if typ == 'Start':
                nr = self.create_knoten(newname)
                self.write_knotenline(current, nr, 'black')
                color = self.call_anal(newname, nr, el)
                self.write_knotenline(nr, current, color)

            if typ == 'End':
                if result == 'True':
                    color = 'green'
                else:
                    color = 'red'
                return color
        return 'end'
    
    def write_table(self):
        el = list(self.tb.event.event_list)
        nr = self.create_knoten('main')
        end = 'go'
        while end != 'end':
            end = self.call_anal('main', nr, el)
