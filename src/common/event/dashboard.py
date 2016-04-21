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
    def __init__(self, tb, eventlogfile, host, user, pw, dbname, tname):
        """
        push tbot results to a mysql database
        after tbot has finished
        """
        self.tb = tb
        self.ev = self.tb.event
        self.eventfile = eventlogfile
        self.fdin = open(self.tb.workdir + '/' + self.eventfile, 'r')
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

    def insert(self, query):
        try:
            self.cursor.execute(query)
        except:
            self.connection.rollback()

        self.connection.commit()
        self.iddb = self.cursor.lastrowid

    def __del__(self):
        self.connection.close()

    def insert_test_into_db(self):
        self.dt = ''
        self.tool = 'unknown'
        self.bina = 'unknown'
        self.defname = 'unknown'
        self.tcname = ''
        self.suc = '1'
        for line in self.fdin:
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
            if tmp[self.ev.id] == 'Toolchain':
                self.tool = ' '.join(tmp[self.ev.value:])

        # Data Insert into the table
        # `stats_img`, `dot_img` missing yet
        # also we need to save the logfile
        query = "INSERT INTO " +  self.tname + " (`test_date`, `toolchain`, `binaryversion`, `defname`, `testcase`, `success`) VALUES ('" + self.dt + "', '" + self.tool + "', '" + self.bina + "', '" + self.defname + "', '" + self.tcname + "', '" + self.suc + "')"
        logging.debug("DB query %s", query)
        self.insert(query)
        # now create the images, and move them to the webserverdirectory
        # ToDo:
        # catch errors
        newdir = self.webdir + '/id_' + str(self.iddb)
        os.system("sudo mkdir " + newdir)
        if (self.tb.create_dot == 'yes'):
            os.system("dot -Tpng tc.dot > tc.png")
            tmp = "sudo cp tc.png " + newdir + "/graph.png"
            os.system(tmp)
        if (self.tb.create_statistic == 'yes'):
            os.system("gnuplot src/files/balkenplot.sem")
            tmp = "sudo cp output.jpg " + newdir + "/statistic.jpg"
            os.system(tmp)
        # at the end, close
        self.fdin.close()
