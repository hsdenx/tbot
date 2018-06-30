# SPDX-License-Identifier: GPL-2.0
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
        self.fd = open(tb.resultdir + '/' + fdfile, 'w')
        self.tc_list = []
        self.ignoretclist = ignorelist

    def _close(self):
        self.fd.close()

    def __del__(self):
        self._close()

    def create_statfile(self):
        """create the statistic file
        """
        try:
            title = self.tb.starttestcase
        except:
            return
        el = list(self.tb.event.event_list)
        self._analyse(el)
        # self._print_list()
        self._write_header()
        self._write_table()
        self._write_bottom()
        self._close()
        w = self.tb.workdir
        r = self.tb.resultdir
        cmd = 'gnuplot -e \'output_file="'+ r + '/output.jpg";input_file="' + r + '/stat.dat";graph_title="' + title + '"\' ' + w + '/src/files/balkenplot.sem'
        os.system(cmd)
 
    def _write_header(self):
        self.fd.write('Name\tFail\tOk\n')
 
    def _write_bottom(self):
        self.fd.write('\n')

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
        el = 'start'
        while el != '':
            el = self._get_next_event(evl)
            if el == '':
                continue
            if el['typ'] != 'EVENT':
                continue
            eid = self._get_event_id(el)
            if eid == 'none':
                continue
            newname = self._get_event_name(el)
            result = el['val']
            ret = self._check_ignore_list(eid, newname, evl)
            if ret == 'ignore':
                continue
            if eid == 'Start' or eid == 'StartFkt':
                eln = self._search_in_list(newname)
                if eln == None:
                    self._add_to_list(newname)
            if eid == 'End':
                eln = self._search_in_list(newname)
                if eln == None:
                    print("Error End not found", newname)
                    continue
                if result == 'True':
                    new = eln[1] + 1
                    newel = eln[0], new, eln[2]
                if result == 'False':
                    new = eln[2] + 1
                    newel = eln[0], eln[1], new
                self._delete_in_list(eln)
                self.tc_list.append(newel)
