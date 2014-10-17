# This file contains default values for all
# variables testcases use ...

try:
    self.term_line_length
except AttributeError:
    self.term_line_length = '200'
    tmp = 'Set terminal line length to ' + self.term_line_length
    self.debugprint(tmp)

try:
    self.read_line_retry
except AttributeError:
    self.read_line_retry = 1

try:
    self.read_end_state_retry
except AttributeError:
    self.read_end_state_retry = 1

try:
    self.tc_return
except AttributeError:
    self.tc_return = True

try:
    self.tc_lx_check_if_cmd_exist_cmdname
except NameError:
    self.tc_lx_check_if_cmd_exist_cmdname = 'none'
except AttributeError:
    self.tc_lx_check_if_cmd_exist_cmdname = 'none'

#src/tc/tc_ub_setenv.py
try:
    self.setenv_name
except AttributeError:
    self.setenv_name = 'tralala'

try:
    self.setenv_value
except AttributeError:
    self.setenv_value = 'hulalahups'

#src/tc/tc_tftp_file.py
try:
    self.tftp_addr_r
except AttributeError:
    self.tftp_addr_r = '21000000'
try:
    self.tftp_file
except AttributeError:
    self.tftp_file = '/tftpboot/at91_taurus/u-boot.bin'

#src/tc/tc_tftp_file.py
try:
    self.tc_lx_mount_dev
except AttributeError:
    self.tc_lx_mount_dev = '/dev/sda1'

try:
    self.tc_lx_mount_fs_type
except AttributeError:
    self.tc_lx_mount_fs_type = 'ext4'

try:
    self.tc_lx_mount_dir
except AttributeError:
    self.tc_lx_mount_dir = '/home/hs/mnt'

try:
    self.tc_lx_bonnie_dev
except AttributeError:
    self.tc_lx_bonnie_dev = self.tc_lx_mount_dir

try:
    self.tc_lx_bonnie_sz
except AttributeError:
    self.tc_lx_bonnie_sz = '968'

try:
    self.ub_load_board_env_addr
except AttributeError:
    self.ub_load_board_env_addr = '0x81000000'

try:
    self.ub_load_board_env_subdir
except AttributeError:
    self.ub_load_board_env_subdir = 'tbot'

try:
    self.tftpboardname
except AttributeError:
    self.tftpboardname = self.boardname
except NameError:
    self.tftpboardname = self.boardname

try:
    self.boardlabname
except AttributeError:
    self.boardlabname = self.boardname
except NameError:
    self.boardlabname = self.boardname

try:
    self.boardlabpowername
except AttributeError:
    self.boardlabpowername = self.boardname
except NameError:
    self.boardlabpowername = self.boardname

try:
    self.tc_ub_dfu_dfu_util_path
except AttributeError:
    self.tc_ub_dfu_dfu_util_path = "/home/hs/zug/dfu-util"

try:
    self.tc_ub_dfu_dfu_util_alt_setting
except AttributeError:
    self.tc_ub_dfu_dfu_util_alt_setting = "Linux"

try:
    self.tc_ub_dfu_dfu_util_downloadfile
except AttributeError:
    self.tc_ub_dfu_dfu_util_downloadfile = "/tmp/dfu_file"

try:
    self.tc_lab_source_dir
except AttributeError:
    self.tc_lab_source_dir = "/work/hs/tbot"

try:
    self.tc_lab_get_uboot_source_git_repo
except AttributeError:
    self.tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"

try:
    self.tc_lab_get_uboot_source_git_branch
except AttributeError:
    self.tc_lab_get_uboot_source_git_branch = "master"

try:
    self.tc_lab_end_git_clone_text
except AttributeError:
    self.tc_lab_end_git_clone_text = "done"

try:
    self.tc_lab_end_git_checkout_text
except AttributeError:
    self.tc_lab_end_git_checkout_text = "error"

try:
    self.tc_lab_toolchain_rev
except AttributeError:
    self.tc_lab_toolchain_rev = "5.4"

try:
    self.tc_lab_toolchain_name
except AttributeError:
    self.tc_lab_toolchain_name = "armv5te"

try:
    self.tc_lab_cp_file_a
except AttributeError:
    self.tc_lab_cp_file_a = "/tmp/gnlmpf"

try:
    self.tc_lab_cp_file_b
except AttributeError:
    self.tc_lab_cp_file_b = "/tmp/gnlmpf2"

try:
    self.tc_ub_ubi_prep_partname
except AttributeError:
    self.tc_ub_ubi_prep_partname = "ubi"

try:
    self.tc_ub_ubi_prep_offset
except AttributeError:
    self.tc_ub_ubi_prep_offset = "none"

try:
    self.tc_ub_ubi_load_addr
except AttributeError:
    self.tc_ub_ubi_load_addr = "14000000"

try:
    self.tc_ub_ubi_load_name
except AttributeError:
    self.tc_ub_ubi_load_name = "kernel"

try:
    self.tc_ub_ubi_create_vol_name
except AttributeError:
    self.tc_ub_ubi_create_vol_name = self.tc_ub_ubi_load_name

try:
    self.tc_ub_ubi_create_vol_sz
except AttributeError:
    self.tc_ub_ubi_create_vol_sz = "600000"

try:
    self.tc_ub_ubi_write_addr
except AttributeError:
    self.tc_ub_ubi_write_addr = self.tc_ub_ubi_load_addr

try:
    self.tc_ub_ubi_write_vol_name
except AttributeError:
    self.tc_ub_ubi_write_vol_name = self.tc_ub_ubi_create_vol_name

try:
    self.tc_lx_gpio_nr
except AttributeError:
    self.tc_lx_gpio_nr = '69'

try:
    self.tc_lx_gpio_dir
except AttributeError:
    self.tc_lx_gpio_dir = 'out'

try:
    self.tc_lx_gpio_val
except AttributeError:
    self.tc_lx_gpio_val = '1'

try:
    self.tc_lx_eeprom_file
except AttributeError:
    self.tc_lx_eeprom_file = '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom'

try:
    self.tc_lx_eeprom_tmp_dir
except AttributeError:
    self.tc_lx_eeprom_tmp_dir = "/tmp/"

#has the eeprom a wp gpio
try:
    self.tc_lx_eeprom_wp_gpio
except AttributeError:
    self.tc_lx_eeprom_wp_gpio = 'none'

#with which value is the eeprom wp
try:
    self.tc_lx_eeprom_wp_val
except AttributeError:
    self.tc_lx_eeprom_wp_val = "0"

#size of the eeprom
#ToDo get this from linux
try:
    self.tc_lx_eeprom_wp_sz
except AttributeError:
    self.tc_lx_eeprom_wp_sz = "4096"

try:
    self.tc_lx_eeprom_wp_obs
except AttributeError:
    self.tc_lx_eeprom_wp_obs = "32"

try:
    self.tc_lx_eeprom_wp_wc
except AttributeError:
    self.tc_lx_eeprom_wp_wc = "128"

try:
    self.tc_lx_cpufreq_frequences
except AttributeError:
    self.tc_lx_cpufreq_frequences = ['294']

try:
    self.tc_lx_check_usb_authorized
except AttributeError:
    self.tc_lx_check_usb_authorized = 'usb 1-1'

try:
    self.tc_lx_work_dir
except AttributeError:
    self.tc_lx_work_dir = "/work/tbot"

try:
    self.tc_lx_check_if_file_exists_name
except AttributeError:
    self.tc_lx_check_if_file_exists_name = "bonnie++-1.03e.tgz"
