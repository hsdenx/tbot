# SPDX-License-Identifier: GPL-2.0
#
import logging
import sys
import os

class web_patchwork(object):
    def __init__(self, tb, webfile):
        self.tb = tb
        self.ev = self.tb.event
        self.webfile = webfile
        self.fd = open(self.tb.workdir + '/' + self.webfile, 'w')
        #print("LJDKJSANDKJASNDKJN open", self.webfile, self.fd)
        #try:
        #    self.fd = open(self.tb.workdir + '/' + self.webfile, 'w')
        #except:
        #    logging.warning("Could not create %s", self.webfile)
        #    sys.exit(1)

    def create_webfile(self):
        #print("LJDKJSANDKJASNDKJN creating", self.webfile)
        self.write_header()
        self.write_table()
        self.write_bottom()
        self.fd.close()

    def write_header(self):
        self.fd.write('<table border=1>\r\n<tr>\r\n')
        self.fd.write('<tr>\r\n')
        self.fd.write('<td>\r\n' + 'Patchnumber' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + 'U-Boot vers' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + 'delegated to' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + 'already applied' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + 'checkpatch clean' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + 'apply clean' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + 'log checkpatch' + '\r\n</td>\r\n')
        self.fd.write('</tr>\r\n')
 
    def write_bottom(self):
        self.fd.write('</tr>\r\n</table>\r\n')

    def write_one_element(self, nr, vers, delto, aa, cc, ac, logcc):
        self.fd.write('<tr>\r\n')
        self.fd.write('<td>\r\n' + '<a href="http://patchwork.ozlabs.org/patch/' + nr + '"> ' + nr + '</a>' + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + vers + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + delto + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + aa + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + cc + '\r\n</td>\r\n')
        self.fd.write('<td>\r\n' + ac + '\r\n</td>\r\n')
        if cc == 'clean' and ac == 'clean':
            logcc = '-'
        self.fd.write('<td>\r\n' + logcc + '\r\n</td>\r\n')
        self.fd.write('</tr>\r\n')
        
    def write_table(self):
        nr = 'unknown'
        aa = 'no'
        cc = 'unknown'
        ac = 'unknown'
        logcc = ''
        for event in self.tb.event.event_list:
            tmp = event.split()
            #print("TMPTMPTMPT", tmp)
            # search for EVENT PW_NR
            if tmp[self.ev.id] == 'PW_NR':
                nr = tmp[self.ev.value]
                logcc = ''
                aa = 'no'
                cc = 'unknown'
                ac = 'unknown'
            if tmp[self.ev.pname] == 'tc_workfd_apply_patchwork_patches.py' and tmp[self.ev.value] == 'r':
                logcc += event.split('ctrl r')[1]
                logcc += '\r\n'

            # search for EVENT PW_CLEAN
            if tmp[self.ev.id] == 'PW_CLEAN':
                if tmp[self.ev.value] == 'True':
                    cc = 'clean'
                else:
                    cc = 'not clean'
            # search for EVENT PW_AA
            if tmp[self.ev.id] == 'PW_AA':
                aa = 'yes'
            # search for EVENT PW_APPLY
            if tmp[self.ev.id] == 'PW_APPLY':
                if tmp[self.ev.value] == 'True':
                    ac = 'clean'
                else:
                    ac = 'not clean'
            if nr != 'unknown' and cc != 'unknown' and ac != 'unknown':
                self.write_one_element(nr, 'unknown', 'unknown', aa, cc, ac, logcc)
                nr = 'unknown'
                aa = 'no'
                cc = 'unknown'
                ac = 'unknown'
                logcc = ''
