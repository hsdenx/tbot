# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Description:
#
# install SPL and u-boot image with imx_usb_installer
# which is installed in tb.config.tc_linux_imx_usb_loader_install_path
#
# first check if tb.config.tc_linux_imx_usb_loader_install_path
# is defined, if not, try to get it with testcase
# tc_linux_imx_usb_loader_install.py
#
# if we find a imx usb loader installation, try to
# load files in tb.config.tc_linux_imx_usb_loader_boot_uboot_files
# from tb.config.tftpdir + tb.config.boardname
# and get into state "u-boot" after all files loaded
# succesfully.
#
# used variables:
#
# - tb.config.tc_linux_imx_usb_loader_install_path
#|  path to imx_usb_loader utility.
#|  default: If not set, try to install imx_usb_loader
#|  utility with tc_linux_imx_usb_loader_install.py
#
# - tb.config.tc_linux_imx_usb_loader_boot_uboot_files
#|  list of files, which get loaded with imx_usb_loader
#|  default:
#|  [
#|       'SPL',
#|      'u-boot-fit.img'
#|  ]
#
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

try:
    tb.config.tc_linux_imx_usb_loader_install_path
except:
    tb.eof_call_tc("tc_linux_imx_usb_loader_install.py")

tb.define_variable('tc_linux_imx_usb_loader_boot_uboot_files', '["SPL", "u-boot-fit.img"]')

logging.info("arg: %s %s", tb.workfd.name, tb.config.tc_linux_imx_usb_loader_install_path)

# power off the board
tb.eof_call_tc("tc_lab_poweroff.py")

# power on the board
tb.eof_call_tc("tc_lab_poweron.py")

def imx_usb_load(tb, c, filen):
    cmd = 'sudo ' + tb.config.tc_linux_imx_usb_loader_install_path + 'imx_usb ' + filen
    tb.write_lx_sudo_cmd_check(c, cmd, tb.config.user, tb.config.ip)

for f in tb.config.tc_linux_imx_usb_loader_boot_uboot_files:
    fn = tb.config.tftpdir + tb.config.boardname + '/' + f
    imx_usb_load(tb, tb.workfd, fn)

tb.set_board_state("u-boot")

tb.end_tc(True)
