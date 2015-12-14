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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_patchwork_number_list.py
# get a list of patchworknumbers
# which are delegated to specific user
# tb.workfd_get_patchwork_number_user
# currently, this testcase reads "http://patchwork.ozlabs.org/project/uboot/list/"
# and filters out the patches, which are for
# tb.workfd_get_patchwork_number_user
# It would be better to login and look for the users
# ToDo list, but I did not find out, how to login ...
from tbotlib import tbot
import urllib2  # the lib that handles the url stuff
import urllib, sys

logging.info("args: workfd: %s %s %s", tb.workfd, tb.workfd_get_patchwork_number_user, tb.tc_workfd_apply_patchwork_patches_blacklist)

tb.tc_workfd_apply_patchwork_patches_list = []
tb.tc_workfd_apply_patchwork_patches_list_title = []

target_url = 'http://patchwork.ozlabs.org/project/uboot/list/'

def analyse_one_page(tb, urll, url, page):
    reg = re.compile("patch_row")
    target = url + "?order=-delegate&page=" + page
    data = urll.urlopen(target) # it's a file like object and works just like a file

    fd =open('result.txt', 'w')
    line = data.readline()
    while line:
        fd.write(line)
        # if line contains "patch_row"
        res = reg.search(line)
        if res:
            nr = line.split(":")[1]
            nr = nr.split('"')[0]
            reg2 = re.compile(nr)
            tmp = False
            for line2 in data: # files are iterable
                fd.write(line2)
                if tmp == True:
                    line2 = line2.split('>')[1]
                    line2 = line2.split('<')[0]
                    break
                res = reg2.search(line2)
                if res:
                    #read one more line -> patchtitle
                    tmp = True

            line = data.readline()
            fd.write(line)
            line = data.readline()
            fd.write(line)
            line = data.readline()
            fd.write(line)
            line = data.readline()
            fd.write(line)
            line = line.split('>')[1]
            line = line.split('<')[0]
            if line == tb.workfd_get_patchwork_number_user:
                applypatch = True
                for black in tb.tc_workfd_apply_patchwork_patches_blacklist:
                    if nr == black:
                        logging.info("blacklisted: %s %s\n" % (nr, line2))
                        applypatch = False
                if applypatch == True:
                    tb.tc_workfd_apply_patchwork_patches_list.append(nr)
                    tb.tc_workfd_apply_patchwork_patches_list_title.append(line2)

        line = data.readline()

    fd.close()

def search_next_page(tb):
    reg2 = re.compile('class="next"')
    page = 'end'
    fd =open('result.txt', 'r')
    tmp = True
    while tmp == True:
        line = fd.readline()
        if line:
            res = reg2.search(line)
            if res:
                line = fd.readline()
                pagetmp = line.split("=")[3]
                page = pagetmp.split('"')[0]
                fd.close()
                return page
        else:
            tmp = False
        
    fd.close()
    return page

#start with page 1 until end
page = "1"
while page != 'end':
    analyse_one_page(tb, urllib2, target_url, page)
    page = search_next_page(tb)

i = 0
for j in tb.tc_workfd_apply_patchwork_patches_list:
    logging.info("nr: %s %s\n" % (tb.tc_workfd_apply_patchwork_patches_list[i], tb.tc_workfd_apply_patchwork_patches_list_title[i]))
    i = i + 1
tb.end_tc(True)
