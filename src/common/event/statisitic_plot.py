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
    """
    create a stat.dat file for creating a TC statistic image
    with gnuplot

    call "gnuplot balkenplot.sem" in tbot workdir after
    a TBot is finsihed

    balkenplot.sem file:
    # set terminal png transparent nocrop enhanced size 450,320 font "arial,8" 
    # set output 'histograms.4.png'

    set boxwidth 0.75 absolute
    set style fill   solid 1.00 border lt -1
    set key outside right top vertical Left reverse noenhanced autotitles columnhead nobox
    set key invert samplen 4 spacing 1 width 0 height 0
    set style histogram rowstacked title  offset character 0, 0, 0
    set datafile missing '-'
    set style data histograms
    set xtics border in scale 0,0 nomirror rotate by -45  offset character 0, 0, 0 autojustify
    set xtics  norangelimit font ",8"
    set xtics   ()
    set title "TC statistic"

    set grid ytics
    set terminal jpeg enhanced size 2048,768
    set output "output.jpg"

    i = 2
    plot 'stat.dat' using 2:xtic(1), for [i=3:3] '' using i

    """
    def __init__(self, tb, fdfile, fdinfile, ignorelist):
        self.dotnr = 0
        self.tb = tb
        self.ev = self.tb.event
        self.fdfile = fdfile
        self.fdinfile = fdinfile
        self.fd = open(tb.workdir + '/' + fdfile, 'w')
        self.fdin = open(tb.workdir + '/' + fdinfile, 'r')
        self.tc_list = []
        self.ignoretclist = ignorelist

    def create_statfile(self):
        self.analyse()
        self.print_list()
        self.write_header()
        self.write_table()
        self.write_bottom()
 
    def write_header(self):
        self.fd.write('Name\tFail\tOk\n')
 
    def write_bottom(self):
        self.fd.write('\n')

    def get_event_typ(self, tmp):
        if tmp[self.ev.id] == 'Start':
            return tmp[self.ev.id]
        if tmp[self.ev.id] == 'End':
            return tmp[self.ev.id]
        return 'none'

    def get_event_name(self, tmp):
        return tmp[self.ev.name]

    def check_ignore_list(self, typ, name):
        if typ != 'Start':
            return 'ok'

        for ign in self.ignoretclist:
            if ign == name:
                # search until End event
                for line in self.fdin:
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

    def delete_in_list(self, val):
        self.tc_list.remove(val)

    def search_in_list(self, name):
        for el in self.tc_list:
            if el[0] == name:
                return el

        return None

    def add_to_list(self, name):
        newel = name, 0, 0
        self.tc_list.append(newel)

    def print_list(self):
        print(self.tc_list)

    def write_table(self):
        for el in self.tc_list:
            tmp = el[0] + '\t' + str(el[2]) + '\t' + str(el[1]) + '\n'
            self.fd.write(tmp)

    def analyse(self):
        for line in self.fdin:
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
            ret = self.check_ignore_list(typ, newname)
            if ret == 'ignore':
                continue
            if typ == 'Start':
                el = self.search_in_list(newname)
                if el == None:
                    self.add_to_list(newname)
            if typ == 'End':
                el = self.search_in_list(newname)
                if el == None:
                    print("Error End not found", newname)
                    continue
                if result == 'True':
                    new = el[1] + 1
                    newel = el[0], new, el[2]
                if result == 'False':
                    new = el[2] + 1
                    newel = el[0], el[1], new
                self.delete_in_list(el)
                self.tc_list.append(newel)
