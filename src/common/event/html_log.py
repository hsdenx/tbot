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

class html_log(object):
    def __init__(self, tb, htmlfile):
        """
        create a html log file after tbot hs finsihed
        """
        self.tb = tb
        self.ev = self.tb.event
        self.htmlfile = htmlfile
        self.fd = open(self.tb.workdir + '/' + self.htmlfile, 'w')
        self.dotnr = 0
        self.htmlid = 0

    def create_htmlfile(self):
        self.write_html_header()
        self.write_log()
        self.write_html_bottom()
        self.fd.close()
 
    def write_html_header(self):
        self.fd.write('<html>\n')
        self.fd.write('<head>\n')
        self.fd.write('<link rel="stylesheet" type="text/css" href="multiplexed_tbotlog.css">\n')
        self.fd.write('<script src="http://code.jquery.com/jquery.min.js"></script>\n')
        self.fd.write('<script>\n')
        self.fd.write('$(document).ready(function () {\n')
        self.fd.write('    // Add expand/contract buttons to all block headers\n')
        self.fd.write('    btns = "<span class=\\"block-expand hidden\\">[+] </span>" +\n')
        self.fd.write('        "<span class=\\"block-contract\\">[-] </span>";\n')
        self.fd.write('    $(".block-header").prepend(btns);\n')
        self.fd.write('\n')
        self.fd.write('    // Pre-contract all blocks which passed, leaving only problem cases\n')
        self.fd.write('    // expanded, to highlight issues the user should look at.\n')
        self.fd.write('    // Only top-level blocks (sections) should have any status\n')
        self.fd.write('    passed_bcs = $(".block-content:has(.status-pass)");\n')
        self.fd.write('    // Some blocks might have multiple status entries (e.g. the status\n')
        self.fd.write('    // report), so take care not to hide blocks with partial success.\n')
        self.fd.write('    passed_bcs = passed_bcs.not(":has(.status-fail)");\n')
        self.fd.write('    passed_bcs = passed_bcs.not(":has(.status-xfail)");\n')
        self.fd.write('    passed_bcs = passed_bcs.not(":has(.status-xpass)");\n')
        self.fd.write('    passed_bcs = passed_bcs.not(":has(.status-skipped)");\n')
        self.fd.write('    // Hide the passed blocks\n')
        self.fd.write('    passed_bcs.addClass("hidden");\n')
        self.fd.write('    // Flip the expand/contract button hiding for those blocks.\n')
        self.fd.write('    bhs = passed_bcs.parent().children(".block-header")\n')
        self.fd.write('    bhs.children(".block-expand").removeClass("hidden");\n')
        self.fd.write('    bhs.children(".block-contract").addClass("hidden");\n')
        self.fd.write('\n')
        self.fd.write('    // Add click handler to block headers.\n')
        self.fd.write('    // The handler expands/contracts the block.\n')
        self.fd.write('    $(".block-header").on("click", function (e) {\n')
        self.fd.write('        var header = $(this);\n')
        self.fd.write('        var content = header.next(".block-content");\n')
        self.fd.write('        var expanded = !content.hasClass("hidden");\n')
        self.fd.write('        if (expanded) {\n')
        self.fd.write('            content.addClass("hidden");\n')
        self.fd.write('            header.children(".block-expand").first().removeClass("hidden");\n')
        self.fd.write('            header.children(".block-contract").first().addClass("hidden");\n')
        self.fd.write('        } else {\n')
        self.fd.write('            header.children(".block-contract").first().removeClass("hidden");\n')
        self.fd.write('            header.children(".block-expand").first().addClass("hidden");\n')
        self.fd.write('            content.removeClass("hidden");\n')
        self.fd.write('        }\n')
        self.fd.write('    });\n')
        self.fd.write('\n')
        self.fd.write('    // When clicking on a link, expand the target block\n')
        self.fd.write('    $("a").on("click", function (e) {\n')
        self.fd.write('        var block = $($(this).attr("href"));\n')
        self.fd.write('        var header = block.children(".block-header");\n')
        self.fd.write('        var content = block.children(".block-content").first();\n')
        self.fd.write('        header.children(".block-contract").first().removeClass("hidden");\n')
        self.fd.write('        header.children(".block-expand").first().addClass("hidden");\n')
        self.fd.write('        content.removeClass("hidden");\n')
        self.fd.write('    });\n')
        self.fd.write('});\n')
        self.fd.write('</script>\n')
        self.fd.write('</head>\n')
        self.fd.write('<body>\n')
        self.fd.write('\n')
        self.fd.write('<tt>\n')
 
    def write_html_bottom(self):
        self.fd.write('</tt>\n')
        self.fd.write('</body>\n')
        self.fd.write('</html>\n')
        self.fd.write('\n')

    def write_tc_start_block(self, name):
        self.htmlid += 1
        self.fd.write('<!-- a testcase -->\n')
        self.fd.write('<div class="section block" id="' + str(self.htmlid) + '">\n')
        self.fd.write('<div class="section-header block-header">' + name + '</div>\n')
        self.fd.write('<div class="section-content block-content">\n')
        self.fd.write('<div class="action">\n')
        self.fd.write('<pre>\n')
        self.fd.write('</pre>\n')
        self.fd.write('</div>\n')
        self.fd.write('\n')

    def write_con_log_block(self, log):
        if log == '':
            return
        self.htmlid += 1
        self.fd.write('<!-- console log of testcase -->\n')
        self.fd.write('<div class="stream block" id="' + str(self.htmlid) + '">\n')
        self.fd.write('<div class="stream-header block-header">console</div>\n')
        self.fd.write('<div class="stream-content block-content">\n')
        self.fd.write('<pre>\n')
        self.fd.write(log)
        self.fd.write('</pre>\n')
        self.fd.write('<div class="stream-trailer block-trailer">End stream: console</div>\n')
        self.fd.write('<div class="status-pass"></div>\n')
        self.fd.write('</div>\n')
        self.fd.write('</div>\n')
        self.fd.write('<!-- end of console log of testcase -->\n')
        self.fd.write('\n')

    def write_ctrl_log_block(self, log):
        if log == '':
            return
        self.htmlid += 1
        self.fd.write('<!-- ctrl log of testcase -->\n')
        self.fd.write('<div class="stream block" id="' + str(self.htmlid) + '">\n')
        self.fd.write('<div class="stream-header block-header">control</div>\n')
        self.fd.write('<div class="stream-content block-content">\n')
        self.fd.write('<pre>\n')
        self.fd.write(log)
        self.fd.write('</pre>\n')
        self.fd.write('<div class="stream-trailer block-trailer">End stream: control</div>\n')
        self.fd.write('<div class="status-pass"></div>\n')
        self.fd.write('</div>\n')
        self.fd.write('</div>\n')
        self.fd.write('<!-- end of control log of testcase -->\n')
        self.fd.write('\n')

    def write_tc_end(self, name, status):
        ststr = 'Failed'
        if status == 'True':
            ststr = 'OK'

        self.fd.write('<div class="section-trailer block-trailer">' + name + '</div>\n')
        if status == 'True':
            self.fd.write('<div class="status-pass">\n')
        else:
            self.fd.write('<div class="status-fail">\n')
        self.fd.write('<pre>' + ststr + '\n')
        self.fd.write('</pre>\n')
        self.fd.write('</div>\n')
        self.fd.write('</div>\n')
        self.fd.write('</div>\n')
        self.fd.write('<!-- end of a testcase -->\n')
        self.fd.write('\n')

    def get_event_typ(self, tmp):
        if tmp[self.ev.id] == 'Boardname':
            return tmp[self.ev.id]
        if tmp[self.ev.id] == 'BoardnameEnd':
            return tmp[self.ev.id]
        if tmp[self.ev.id] == 'log':
            return tmp[self.ev.id]
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

    def write_testcase(self, name, el):
        # write start of tc block need name
        if name != 'StartHTML':
            self.write_tc_start_block(name)

        conlog =''
        ctrlog =''
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
            tc_name = self.get_event_name(tmp)

            if typ == 'Start' or typ == 'Boardname':
                # write con block need log
                self.write_con_log_block(conlog)
                # write ctrl need log
                self.write_ctrl_log_block(ctrlog)
                # write end of tc block (name, status)
                conlog = ''
                ctrlog = ''
                self.write_testcase(tc_name, el)

            # get status (end of TC) parse "End" or "BoardnameEnd" check if name == name !
            if typ == 'End' or typ == 'BoardnameEnd':
                if tc_name != name:
                    print("not sync with tc name\n", tc_name, name)
                status = tmp[self.ev.value]
                # write con block need log
                self.write_con_log_block(conlog)
                # write ctrl need log
                self.write_ctrl_log_block(ctrlog)
                # write end of tc block (name, status)
                self.write_tc_end(name, status)
                return
                
            if typ == 'log':
                # get list of tb_con log
                # get list of tb_ctrl log
                # print("** ", line)
                loglin = line.split("tb_con r ")
                if len(loglin) == 2:
                    conlog += loglin[1]
                loglin = line.split("tb_con re ")
                if len(loglin) == 2:
                    conlog += loglin[1]
                ctrlin = line.split("tb_ctrl r ")
                if len(ctrlin) == 2:
                    ctrlog += ctrlin[1]
                continue

    def write_log(self):
        el = self.tb.event.event_list
        self.write_testcase('StartHTML', el)
