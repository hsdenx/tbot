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
        create a doc for tbot testcases
        """
        self.subdir = subdir
        self.tcfile = 'doc/sphinx/source/testcases.rst'
        self.varfile = 'doc/sphinx/source/variables.rst'
        self.workdir = os.getcwd()
        self.fdt = open(self.workdir + '/' + self.tcfile, 'w')
        self.fdv = open(self.workdir + '/' + self.varfile, 'w')

    def create_htmlfile(self):
        self.write_tc_header()
        self.write_doc()
        self.write_tc_bottom()
        self.write_var_header()
        self.write_doc_var()
        self.write_var_bottom()
        self.fdt.close()
        self.fdv.close()

    def write_tc_header(self):
        self.fdt.write('Documentation of all Testcases\n')
        self.fdt.write('==============================\n')
        self.fdt.write('\n')

    def write_tc_subheader(self, name, level):
        self.fdt.write('\n')
        self.fdt.write(name)
        self.fdt.write('\n')
	for c in name:
            self.write_level(level)

        self.fdt.write('\n')
        self.fdt.write('\n')
 
    def write_tc_bottom(self):
        self.fdt.write('\n')

    def write_var_header(self):
        self.fdv.write('Documentation of all Variables\n')
        self.fdv.write('==============================\n')
        self.fdv.write('\n')
 
    def write_var_bottom(self):
        self.fdv.write('\n')

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
        tmp = '_' + new
        return tmp

    def to_id_var(self, tmp):
        tmp = tmp.strip()
        new = tmp.replace('/', '_')
        new = new.replace('.', '_')
        if new.startswith('tb'):
            tmp = '_' + new
        else:
            tmp = '_tb_config_' + new
        return tmp

    def get_tc_description(self, filen):
        # scan for TC description
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
        # ToDo remove reference to own tc ...
        link_tc = ''
        link_var = ''
        link_http = ''
        for line in des:
            tmp = line.split(' ')
            i = 0
            if len(tmp) > 0:
                last = len(tmp) - 1
                lastwasreturn = 0
                for el in tmp:
                    # found reference to other testcase
                    if el.startswith('tc_'):
                        dirp = self.find_tc_path(el.rstrip('\n'))
                        ref = self.to_id(dirp) + self.to_id(el.rstrip('\n'))
                        link_tc += ':ref:`' + ref[1:] + '`.\n'
                    # found reference to variable
                    if el.startswith('tb.'):
                        link_var += ':ref:`' + self.to_id_var(el)[1:] + '`.\n'
                    # found reference to http
                    if el.startswith('http'):
                        link_http += el + '\n'

                    i += 1
                des[j] = ' '.join(tmp)
            j += 1

        if len(des) > 0:
            for line in des:
                self.fdt.write('  ' + line)
        self.fdt.write('\n')
        if link_tc != '':
            self.fdt.write('used Testcases:\n\n')
            for line in link_tc:
                self.fdt.write(line)
        self.fdt.write('\n')
        if link_var != '':
            self.fdt.write('used config variables:\n\n')
            for line in link_var:
                self.fdt.write(line)
        self.fdt.write('\n')
        if link_http != '':
            self.fdt.write('links:\n\n')
            for line in link_http:
                self.fdt.write(line)
        self.fdt.write('\n')
        self.fdt.write('\n')
        self.fdt.write('https://github.com/hsdenx/tbot/tree/master/'+ filen)
        self.fdt.write('\n')
        # add link to testcase on github

    def write_level(self, level):
        if level == 0:
            self.fdt.write('-')
        elif level == 1:
            self.fdt.write(',')
        else:
            self.fdt.write('.')

    def analyse_tc(self, filen, level):
        # write reference
        self.fdt.write('\n')
        tmp = '.. ' + self.to_id(filen) + ':\n'
        self.fdt.write(tmp)
        self.fdt.write('\n')
        # write TC name
        self.fdt.write(filen + '\n')
        for x in filen:
            self.write_level(level - 1)
        self.fdt.write('\n')
        self.fdt.write('\n')
        self.fdt.write('::\n')
        self.fdt.write('\n')
        # here write the text
        self.get_tc_description(filen)
        self.fdt.write('\n')

    def write_onedocdir(self, dirp, level):
        # write header
        # self.write_start_block(dirp)
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
		self.write_tc_subheader(s, level)
                self.write_onedocdir(s, level + 1)

        if len(files) > 0:
            for f in sorted(files):
                self.analyse_tc(f, level + 1)

        # write end
        # self.write_end_block(dirp)

    def write_doc(self):
        self.write_onedocdir(self.subdir, 0)

    def write_var(self, name, des):
        # write reference
        self.fdv.write('\n')
        tmp = '.. ' + self.to_id_var(name) + ':\n'
        self.fdv.write(tmp)
        self.fdv.write('\n')
        # write var name
        self.fdv.write(name + '\n')
        for x in name:
            self.fdv.write('-')
        self.fdv.write('\n')
 
        # here write the text
        self.fdv.write('\n')
        self.fdv.write('::\n')
        self.fdv.write('\n')
        for line in des:
            self.fdv.write('  ' + line.lstrip())
        self.fdv.write('\n')

    def write_docdir_var(self, dirp):
        # write header
        # self.write_start_block('write_docdir_var Default Variables')

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
        # self.write_end_block('Default Variables')

    def write_start_block_var(self, name):
        self.fdv.write('<!-- start block var ' + name + ' -->\n')
        self.fdv.write('<!-- start block var ' + self.to_id(name) + ' -->\n')
        self.fdv.write('\n')

    def write_end_block_var(self, name):
        self.fdv.write('end block var ' + name + '\n')

    def write_doc_var(self):
        self.write_docdir_var('src/common/')

doc = create_doc('src/tc')
doc.create_htmlfile()
