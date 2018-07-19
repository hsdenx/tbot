# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get a list of patchworknumbers
# which are delegated to specific user
# tb.config.workfd_get_patchwork_number_user
# currently, this testcase reads "http://patchwork.ozlabs.org/project/uboot/list/"
# and filters out the patches, which are for
# tb.config.workfd_get_patchwork_number_user
# It would be better to login and look for the users
# ToDo list, but I did not find out, how to login ...
# ignore patches on blacklist:
# tb.config.tc_workfd_apply_patchwork_patches_blacklist
# also you can set the patch order with:
# tb.config.tc_workfd_get_patchwork_number_list_order
#
# used variables
#
# - tb.config.workfd_get_patchwork_number_user
#| patchwork username
#| default: 'hs'
#
# - tb.config.tc_workfd_apply_patchwork_patches_blacklist
#| patchwork numbers, which get ignored
#| default: '[]'
#
# - tb.config.tc_workfd_get_patchwork_number_list_order
#| ?order= parameter for request patchwork page
#| default: '-delegate'
#
# End:

from tbotlib import tbot
import urllib2  # the lib that handles the url stuff
import urllib, sys

tb.define_variable('workfd_get_patchwork_number_user', 'hs')
tb.define_variable('tc_workfd_apply_patchwork_patches_blacklist', '[]')
tb.define_variable('tc_workfd_get_patchwork_number_list_order', '-delegate')
tb.define_variable('tc_workfd_apply_patchwork_patches_list_hand', '[]')
logging.info("args: workfd: %s", tb.workfd)

tb.config.tc_workfd_apply_patchwork_patches_list = []
tb.config.tc_workfd_apply_patchwork_patches_list_title = []

target_url = 'http://patchwork.ozlabs.org/project/uboot/list/'

def analyse_one_page(tb, urll, url, page):
    reg = re.compile("patch_row")
    target = url + "?order=" + tb.config.tc_workfd_get_patchwork_number_list_order + "&page=" + page
    data = urll.urlopen(target) # it's a file like object and works just like a file

    fd = open('result.txt', 'w')
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
                    # line2 contains now patchtitle
                    patchtitle = line2.split('\n')[0]
                    break
                res = reg2.search(line2)
                if res:
                    #read one more line -> patchtitle
                    tmp = True

            # read delegated to
            # there are 3 lines with "text-nowrap"
            reg2 = re.compile('text-nowrap')
            tmp = False
            i = 0
            for line2 in data: # files are iterable
                fd.write(line2)
                res = reg2.search(line2)
                if res:
                    i += 1
                if i == 3:
                   break

            # plus one more line with a href ...
            line = data.readline()
            fd.write(line)
            # finally read the line with the delegated to
            line = data.readline()
            fd.write(line)
            line = line.split('>')[1]
            line = line.split('<')[0]
            if line == tb.config.workfd_get_patchwork_number_user or tb.config.workfd_get_patchwork_number_user == 'all':
                applypatch = True
                for black in tb.config.tc_workfd_apply_patchwork_patches_blacklist:
                    if nr == black:
                        logging.info("blacklisted: %s %s\n" % (nr, patchtitle))
                        applypatch = False
                if applypatch == True:
                    tb.config.tc_workfd_apply_patchwork_patches_list.append(nr)
                    tb.config.tc_workfd_apply_patchwork_patches_list_title.append(patchtitle)

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
for j in tb.config.tc_workfd_apply_patchwork_patches_list:
    logging.info("nr: %s %s\n" % (tb.config.tc_workfd_apply_patchwork_patches_list[i], tb.config.tc_workfd_apply_patchwork_patches_list_title[i]))
    i += 1
tb.end_tc(True)
