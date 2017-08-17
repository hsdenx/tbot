# create doc for all testcases
#
import os
import sys
import os.path
from fnmatch import fnmatch
from stat import *

class create_doc(object):
    def __init__(self, subdir):
        """
        create a html doc for tbot testcases
        """
        self.subdir = subdir
        self.htmlfile = 'doc/sphinx/source/_static/doc_testcases.html'
        self.workdir = os.getcwd()
        self.fd = open(self.workdir + '/' + self.htmlfile, 'w')

    def create_htmlfile(self):
        self.write_html_header()
        self.write_doc()
        self.write_doc_var()
        self.write_html_bottom()
        self.fd.close()
  
    def write_html_header(self):
        self.fd.write('<html>\n')
        self.fd.write('<head>\n')
        self.fd.write('<link rel="stylesheet" type="text/css" href="multiplexed_tbotdoc.css">\n')
        self.fd.write('<script src="http://code.jquery.com/jquery.min.js"></script>\n')
        self.fd.write('<script>\n')
        self.fd.write('$(document).ready(function () {\n')
        self.fd.write('    // Add expand/contract buttons to all block headers\n')
        self.fd.write('    btns = "<span class=\\"block-expand hidden\\">[+] </span>" +\n')
        self.fd.write('        "<span class=\\"block-contract\\">[-] </span>";\n')
        self.fd.write('    $(".block-header").prepend(btns);\n')
        self.fd.write('\n')
        self.fd.write('    // Add expand/contract buttons to all block headers dir\n')
        self.fd.write('    btnsd = "<span class=\\"block-expand hidden\\">[+] </span>" +\n')
        self.fd.write('        "<span class=\\"block-contract\\">[-] </span>";\n')
        self.fd.write('    $(".block-header-dir").prepend(btns);\n')
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
        self.fd.write('    // Flip the expand/contract button hiding for those blocks.\n')
        self.fd.write('    bhsd = passed_bcs.parent().children(".block-header-dir")\n')
        self.fd.write('    bhsd.children(".block-expand").removeClass("hidden");\n')
        self.fd.write('    bhsd.children(".block-contract").addClass("hidden");\n')
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
        self.fd.write('    // Add click handler to block headers dir.\n')
        self.fd.write('    // The handler expands/contracts the block.\n')
        self.fd.write('    $(".block-header-dir").on("click", function (e) {\n')
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

    def find_tc_path(self, tcn):
        for dirpath, dirnames, filenames in os.walk(self.subdir):
            for filename in [f for f in filenames if f.endswith(".py")]:
                if filename == tcn:
                    return dirpath

        print("Error: Could not find TC ", tcn);
        return ''

    def to_id(self, tmp):
        new = tmp.replace('/', '_')
        new = new.replace('.', '_')
        return new

    def to_id_var(self, tmp):
        tmp = tmp.strip()
        new = tmp.replace('/', '_')
        new = new.replace('.', '_')
        if new.startswith('config_'):
            new = 'var_' + new
        else:
            new = 'var_config_' + new
        return new

    def get_file_description(self, filen):
        f = open(self.workdir + '/' + filen, 'r')
        found = 0
        des = []
        for line in f:
            if 'Description:' in line:
                found = 1
            elif 'End:' in line:
                found = 0
            else:
                if found == 1:
                    des.append(line)
        f.close()

        # scan for links to other testcases
        j = 0
        for line in des:
            tmp = line.split(' ')
            i = 0
            if len(tmp) > 0:
                last = len(tmp) - 1
                lastwasreturn = 0
                for el in tmp:
                    if el.startswith('tc_'):
                        if el[-1] == '\n':
                            lastwasreturn = 1
                        dirp = self.find_tc_path(el.rstrip('\n')) + '/'
                        nw = '<a href="#' + self.to_id(dirp) + self.to_id(el.rstrip('\n')) + '">' + el.rstrip('\n') + '</a>'
                        tmp[i] = nw
                        if lastwasreturn:
                            tmp[i] += '\n'
                    if el.startswith('tb.'):
                        if el[-1] == '\n':
                            lastwasreturn = 1
                        nw = '<a href="#' + self.to_id_var(el[3:].rstrip('\n')) + '">' + el.rstrip('\n') + '</a>'
                        tmp[i] = nw
                        if lastwasreturn:
                            tmp[i] += '\n'

                    if el.startswith('http'):
                        if el[-1] == '\n':
                            lastwasreturn = 1
                        nw = '<a href="' + el.rstrip('\n') + '">' + el.rstrip('\n') + '</a>'
                        tmp[i] = nw
                        if lastwasreturn:
                            tmp[i] += '\n'


                    i += 1
                des[j] = ' '.join(tmp)
            j += 1

        if len(des) > 0:
            for line in des:
                self.fd.write(line)

    def write_new_file(self, filen):
        self.fd.write('<!-- one testcase ' + filen + ' -->\n')
        self.fd.write('<div class="stream block" id="' + self.to_id(filen) + '">\n')
        self.fd.write('<div class="stream-header block-header">' + filen + '</div>\n')
        self.fd.write('<div class="stream-content block-content">\n')
        self.fd.write('<pre>\n')
        # here write the text
        self.get_file_description(filen)
        self.fd.write('</pre>\n')
        self.fd.write('<div class="stream-trailer block-trailer">End stream: ' + filen + ' </div>\n')
        self.fd.write('<div class="status-pass"></div>\n')
        self.fd.write('</div>\n')
        self.fd.write('</div>\n')
        self.fd.write('<!-- end of one testcase ' + filen + ' -->\n')
        self.fd.write('\n')

    def write_start_block(self, name):
        self.fd.write('<!-- a testcase dir ' + self.to_id(name) + ' -->\n')
        self.fd.write('<div class="section block" id="' + name + '">\n')
        self.fd.write('<div class="section-header block-header-dir">' + name + '</div>\n')
        self.fd.write('<div class="section-content block-content">\n')
        self.fd.write('<div class="action">\n')
        self.fd.write('<pre>\n')
        self.fd.write('</pre>\n')
        self.fd.write('</div>\n')
        self.fd.write('\n')

    def write_end_block(self, name):
        status = 'True'
        ststr = ''
        if status == 'True':
            ststr = ''
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
        self.fd.write('<!-- end of a testcase dir ' + name + ' -->\n')
        self.fd.write('\n')

    def write_onedocdir(self, dirp):
        # write header
        self.write_start_block(dirp)
        files = []
        subdirs = []
        # for all files and dir in dirp
        for f in os.listdir(dirp):
            pathname = os.path.join(dirp, f)
            mode = os.stat(pathname)[ST_MODE]
            if S_ISDIR(mode):
                subdirs.append(pathname)
            elif S_ISREG(mode):
                if fnmatch(pathname, '*.py'):
                    files.append(pathname)
            else:
                print("Error no dir, nor file", pathname, mode)

        if len(subdirs) > 0:
            for s in sorted(subdirs):
                self.write_onedocdir(s)

        if len(files) > 0:
            for f in sorted(files):
                self.write_new_file(f)

        # write end
        self.write_end_block(dirp)

    def write_doc(self):
        self.write_onedocdir(self.subdir)

    def write_var(self, name, des):
        self.fd.write('<!-- one default var ' + name + ' -->\n')
        self.fd.write('<div class="stream block" id="' + self.to_id_var(name) + '">\n')
        self.fd.write('<div class="stream-header block-header">' + name + '</div>\n')
        self.fd.write('<div class="stream-content block-content">\n')
        self.fd.write('<pre>\n')
        # here write the text
        # ToDo add link to other default var, or testcases
        # like in get_file_description
        for line in des:
            self.fd.write(line.lstrip())
        self.fd.write('</pre>\n')
        self.fd.write('<div class="stream-trailer block-trailer">End stream: ' + name + ' </div>\n')
        self.fd.write('<div class="status-pass"></div>\n')
        self.fd.write('</div>\n')
        self.fd.write('</div>\n')
        self.fd.write('<!-- end of one default var ' + name + ' -->\n')
        self.fd.write('\n')


    def write_docdir_var(self, dirp):
        # write header
        self.write_start_block('Default Variables')

        fdv = open(self.workdir + '/' + dirp + '/default_vars.py', 'r')
        var = ''
        des = []
        for line in fdv:
            if line[0] == '#':
                continue
            if line[0] == '\n':
                continue
            if "=" in line:
                if des != []:
                    self.write_var(var, des)
                    var = ''
                    des = []
                tmp = line.split('=')
                var = tmp[0]

            des.append(line)

        fdv.close()
        # write end
        self.write_end_block('Default Variables')

    def write_start_block_var(self, name):
        self.fd.write('<!-- a testcase dir ' + self.to_id(name) + ' -->\n')
        self.fd.write('<div class="section block" id="' + name + '">\n')
        self.fd.write('<div class="section-header block-header-dir">' + name + '</div>\n')
        self.fd.write('<div class="section-content block-content">\n')
        self.fd.write('<div class="action">\n')
        self.fd.write('<pre>\n')
        self.fd.write('</pre>\n')
        self.fd.write('</div>\n')
        self.fd.write('\n')

    def write_end_block_var(self, name):
        status = 'True'
        ststr = ''
        if status == 'True':
            ststr = ''
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
        self.fd.write('<!-- end of a testcase dir ' + name + ' -->\n')
        self.fd.write('\n')

    def write_doc_var(self):
        self.write_docdir_var('src/common/')

doc = create_doc('src/tc')
doc.create_htmlfile()
