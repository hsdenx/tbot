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
        self.htmlfile = 'doc/sphinx/source/_static/doc_testcases.rst'
        self.htmlfile = 'doc/sphinx/source/testcases.rst'
        self.workdir = os.getcwd()
        self.fd = open(self.workdir + '/' + self.htmlfile, 'w')
        self.level = 1

    def create_htmlfile(self):
        self.write_rst_header()
        self.write_doc()
        self.write_doc_var()
        self.write_rst_bottom()
        self.fd.close()
 
    def write_underline(self, string, symbol):
        for c in string:
            self.fd.write(symbol)
        self.fd.write('\n')

    def write_title(self, title):
        t = self.to_id(title)
        self.fd.write('.. _' + t + ':\n')
        self.fd.write('\n')
        title = title + '\n'
        if self.level == 1:
            self.write_underline(title.strip(), '=')
            self.fd.write(title)
            self.write_underline(title.strip(), '=')
        elif self.level == 2:
            self.write_underline(title.strip(), '-')
            self.fd.write(title)
            self.write_underline(title.strip(), '-')
        elif self.level == 3:
            self.write_underline(title.strip(), '*')
            self.fd.write(title)
            self.write_underline(title.strip(), '*')
        elif self.level == 4:
            self.fd.write(title)
            self.write_underline(title.strip(), '=')
        elif self.level == 5:
            self.fd.write(title)
            self.write_underline(title.strip(), ',')
        elif self.level == 6:
            self.fd.write(title)
            self.write_underline(title.strip(), ';')
        elif self.level == 7:
            self.fd.write(title)
            self.write_underline(title.strip(), '.')
        elif self.level == 8:
            self.fd.write(title)
            self.write_underline(title.strip(), '-')
        elif self.level == 9:
            self.fd.write(title)
            self.write_underline(title.strip(), '+')
        elif self.level == 10:
            self.fd.write(title)
            self.write_underline(title.strip(), '<')
        elif self.level == 11:
            self.fd.write(title)
            self.write_underline(title.strip(), '>')
        elif self.level == 12:
            self.fd.write(title)
            self.write_underline(title.strip(), '[')
        elif self.level == 13:
            self.fd.write(title)
            self.write_underline(title.strip(), ']')
        elif self.level == 14:
            self.fd.write(title)
            self.write_underline(title.strip(), '!')
        elif self.level == 15:
            self.fd.write(title)
            self.write_underline(title.strip(), '%')
        elif self.level == 16:
            self.fd.write(title)
            self.write_underline(title.strip(), '(')
        elif self.level == 17:
            self.fd.write(title)
            self.write_underline(title.strip(), ')')
        elif self.level == 18:
            self.fd.write(title)
            self.write_underline(title.strip(), '$')
        elif self.level == 19:
            self.fd.write(title)
            self.write_underline(title.strip(), '?')
        elif self.level == 20:
            self.fd.write(title)
            self.write_underline(title.strip(), '_')
        elif self.level == 21:
            self.fd.write(title)
            self.write_underline(title.strip(), '@')
        else:
            print("ERROR do not know level ", self.level)

    def write_rst_header(self):
        self.write_title('Testcases Documentation')
        self.fd.write('\n')
        self.fd.write('Simply a documentation for all testcases, found in ' + self.subdir + '\n')
        self.fd.write('\n')
 
    def write_rst_bottom(self):
        self.fd.write('The End\n')
        self.fd.write('\n')

    def find_tc_path(self, tcn):
        for dirpath, dirnames, filenames in os.walk(self.subdir):
            for filename in [f for f in filenames if f.endswith(".py")]:
                if filename == tcn:
                    return dirpath

        print("Error: Could not find TC ", tcn);
        return ''

    def to_id(self, tmp):
        new = os.path.basename(tmp)
        new = new.replace('.', '_')
        new = new.replace(' ', '_')
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

    def find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)

    def add_link_2_testcase(self, line):
        if ('tbot.py' in line):
            return line

        if not ('.py' in line) and not ('tb.config.' in line):
            return line

        orgline = line
        # refer to testcase
        line = line.replace('.py', '_py_')
        # add reference for variables
        # variables are defined with beginning '- '
        if line[0] == '-':
            rest = line.replace('- tb.config.', '')
            rest = rest.strip()
            newline = '.. ' + '_tb.config.' + rest + ':\n'
            newline += '\n'
            newline += orgline
            line = newline
        else:
            found = list(self.find_all(line, 'tb.config.'))
            while found:
                for f in found:
                    tmp = line[int(f):]
                    tmp = tmp.split()[0]
                    line = line.replace(tmp, tmp.replace('tb.config.', 'tb_config_') + '_')
                    break
                found = list(self.find_all(line, 'tb.config.'))
            line = line.replace('tb_config_', 'tb.config.')

        return line

    def get_file_description(self, filen):
        f = open(self.workdir + '/' + filen, 'r')
        found = 0
        for line in f:
            if 'Description:' in line:
                found = 1
            elif 'End:' in line:
                found = 0
            else:
                if found == 1:
                    newline = True
                    line = line.replace('#', '')
                    line = line.lstrip()
                    if len(line):
                        if line[0] == '-' or line[0] == '|':
                            newline = False
                    line = line.replace('*', '\\*')
                    line = self.add_link_2_testcase(line)
                    self.fd.write(line)
                    if newline:
                        self.fd.write('\n')

        f.close()
        return

    def write_new_file(self, filen):
        self.write_title(filen.replace(self.subdir, ''))
        self.fd.write('\n')
        self.fd.write('https://github.com/hsdenx/tbot/blob/master/' + filen + '\n')
        self.fd.write('\n')
        self.get_file_description(filen)

    def write_end_file(self, name):
        self.fd.write('\n')
        self.fd.write('------------------------------------------------')
        self.fd.write('\n')
        self.fd.write('\n')

    def write_start_block(self, name):
        self.level = self.level + 1
        self.write_title('Directory ' + name.replace(self.subdir, ''))
        self.fd.write('\n')

    def write_end_block(self, name):
        self.level = self.level - 1
        self.fd.write('\n')

    def write_onedocdir(self, dirp):
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

        self.write_start_block(dirp)
        if len(subdirs) > 0:
            for s in sorted(subdirs):
                self.write_onedocdir(s)

        if len(files) > 0:
            self.level = self.level + 1
            for f in sorted(files):
                self.write_new_file(f)
                self.write_end_file(f)
            self.level = self.level - 1

        # write end
        self.write_end_block(dirp)

    def write_doc(self):
        self.write_onedocdir(self.subdir)

    def write_docdir_var(self, dirp):
        # write header
        pass

    def write_doc_var(self):
        self.write_docdir_var('src/common/')

doc = create_doc('src/tc/')
doc.create_htmlfile()
