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
import MySQLdb

class dashboard(object):
    """extract tbot results to a mysql database
    after tbot has finished

    Prerequisites:

    MySQLdb python module is needed, install it for
    example on the raspberry pi with:

    ::

      apt-get install python-mysqldb

    If tb.config.create_dot == 'yes' then you need the dot

    command, please install this, see for example:

    http://askubuntu.com/questions/97552/how-to-install-dot-provided-by-graphviz

    If tb.config.create_statistic == 'yes' you need the gnuplot

    command. See an example for installing gnuplot here:

    http://askubuntu.com/questions/340579/how-to-install-gnuplot-in-ubuntu

    The dashboard backend also collects information from other backends
    (if they are enabled) and stores them in "webdir".
    Currently this is a fix place, need here some work to make this
    configurable. Currently it is placed at "/var/www/html", and subdir
    "tbot" plus current MYSQL ID "id_%d" ... 

    - **parameters**, **types**, **return** and **return types**::
    :param arg1: tb
    :param arg2: host
    :param arg3: username
    :param arg4: pw
    :param arg5: dbname
    :param arg5: tname
    """
    def __init__(self, tb, host, user, pw, dbname, tname):
        self.tb = tb
        self.ev = self.tb.event
        self.host = host
        self.user = user
        self.pw = pw
        self.dbname = dbname
        self.tname = tname
        self.webdir = '/var/www/html'
        try:
            self.connection = MySQLdb.connect(self.host, self.user, self.pw, self.dbname)
        except:
            logging.warn("Could not connect to host %s", self.host)

        try:
            self.cursor = self.connection.cursor()
        except:
            logging.warn("Could not connect to DB %s", self.dbname)

    def _insert(self, query):
        try:
            self.cursor.execute(query)
        except:
            self.connection.rollback()

        self.connection.commit()
        self.iddb = self.cursor.lastrowid

    def __del__(self):
        self.connection.close()

    def _get_next_event(self, el):
        if len(el) == 0:
            return ''

        ret = el[0]
        el.pop(0)
        return ret

    def insert_test_into_db(self):
        """starts with filling the DB
        """
        evl = list(self.tb.event.event_list)
        self.dt = ''
        self.tool = 'unknown'
        self.bina = 'unknown'
        self.defname = 'unknown'
        self.lx_defname = 'unknown'
        self.tcname = ''
        self.testpypatch = ''
        self.uboot_src_path = ''
        self.linux_src_path = ''
        self.suc = '1'
        line = 'start'
        while line != '':
            line = self._get_next_event(evl)
            tmp = line.split()
            if tmp == []:
                continue
            if tmp[self.ev.typ] != 'EVENT':
                continue
            if tmp[self.ev.id] == 'none':
                continue
            if tmp[self.ev.id] == 'Start':
                if tmp[self.ev.pname] == '<module>':
                    if  self.tcname == '':
                        self.tcname = tmp[self.ev.name]
            if tmp[self.ev.id] == 'End':
                if tmp[self.ev.name] == self.tcname:
                    if tmp[self.ev.value] == 'False':
                        self.suc = '0'
            if tmp[self.ev.id] == 'Boardname':
                self.dt = tmp[self.ev.date] + " " + tmp[self.ev.time]
            if tmp[self.ev.id] == 'UBOOT_DEFCONFIG':
                self.defname = tmp[self.ev.value]
            if tmp[self.ev.id] == 'UBOOT_SRC_PATH':
                self.uboot_src_path = tmp[self.ev.value]
            if tmp[self.ev.id] == 'LINUX_DEFCONFIG':
                self.lx_defname = tmp[self.ev.value]
            if tmp[self.ev.id] == 'LINUX_SRC_PATH':
                self.linux_src_path = tmp[self.ev.value]
            if tmp[self.ev.id] == 'UBOOT_TEST_PY':
                self.testpypatch = tmp[self.ev.value]
            if tmp[self.ev.id] == 'UBOOT_VERSION':
                if self.bina == 'unknown':
                    self.bina = ' '.join(tmp[self.ev.value:])
                else:
                    vers = ' '.join(tmp[self.ev.value:])
                    if vers not in self.bina:
                        self.bina += ' <br> '
                        self.bina += vers
            if tmp[self.ev.id] == 'Toolchain':
                self.tool = ' '.join(tmp[self.ev.value:])

        defn = self.defname
        if (self.lx_defname != 'unknown'):
            if (defn == 'unknown'):
                defn = self.lx_defname
            else:
                defn += ' ' + self.lx_defname

        # Data Insert into the table
        # `stats_img`, `dot_img` missing yet
        # also we need to save the logfile
        query = "INSERT INTO " +  self.tname + " (`test_date`, `toolchain`, `binaryversion`, `defname`, `testcase`, `success`) VALUES ('" + self.dt + "', '" + self.tool + "', '" + self.bina + "', '" + defn + "', '" + self.tcname + "', '" + self.suc + "')"
        logging.debug("DB query %s", query)
        self._insert(query)
        # now create the images, and move them to the webserverdirectory
        # ToDo:
        # catch errors
        newdir = self.webdir + '/tbot/id_' + str(self.iddb)
        os.system("mkdir " + newdir)
        os.system("chmod 755 " + newdir)
        if (self.tb.config.create_dot == 'yes'):
            os.system("dot -Tpng " + self.tb.workdir + "/tc.dot > " + self.tb.workdir + "/tc.png")
            tmp = "cp " + self.tb.workdir + "/tc.png " + newdir + "/graph.png"
            os.system(tmp)
        if (self.tb.config.create_statistic == 'yes'):
            os.system("gnuplot " + self.tb.workdir + "/src/files/balkenplot.sem")
            tmp = "cp " + self.tb.workdir + "/output.jpg " + newdir + "/statistic.jpg"
            os.system(tmp)
        if (self.tb.config.create_html_log == 'yes'):
            tmp = "cp " + self.tb.workdir + "/log/html_log.html " + newdir + "/html_log.html"
            os.system(tmp)
            tmp = "cp " + self.tb.workdir + "/log/multiplexed_tbotlog.css " + newdir + "/multiplexed_tbotlog.css"
            os.system(tmp)
        if self.testpypatch != '':
            rem = self.testpypatch + '/test-log.html'
            loc = newdir + '/test-log.html'
            self.tb.c_ctrl.copy_file(rem, loc)
            rem = self.testpypatch + '/multiplexed_log.css'
            loc = newdir + '/multiplexed_log.css'
            self.tb.c_ctrl.copy_file(rem, loc)
        if self.uboot_src_path != '':
            rem = self.uboot_src_path + '/.config'
            loc = newdir + '/.config'
            self.tb.c_ctrl.copy_file(rem, loc)
        if self.linux_src_path != '':
            rem = self.linux_src_path + '/.config'
            loc = newdir + '/.config'
            self.tb.c_ctrl.copy_file(rem, loc)

        tmp = "cp " + self.tb.logfilen + " " + newdir + "/tbot.log"
        os.system(tmp)
        os.system("chmod 744 " + newdir + "/.config")
        os.system("chmod 744 " + newdir + "/*")
