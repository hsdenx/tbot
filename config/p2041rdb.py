# tbot configuration
# for the p2041rdb board
boardname = 'p2041rdb'
debug=False
debugstatus=True
loglevel='INFO'

wdt_timeout = '3600'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

#create_dot = 'yes'
#create_statistic = 'yes'
#create_dashboard = 'yes'
#create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
#tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
#tc_workfd_connect_with_kermit_rlogin = 'rlogin metis fipad'
#tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
#board_has_debugger = 1
#lab_bdi_upd_uboot_bdi_prompt = 'P2041#0>'
#lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi15'

setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'

tc_lab_get_uboot_source_git_repo = '/home/hs/IAI/boottime/u-boot'
tc_lab_get_uboot_source_git_branch = '20160809-uboot'

tc_lab_toolchain_rev = '5.4'
tc_lab_toolchain_name = 'powerpc'

tc_ub_create_reg_file_name = 'src/files/fipad_ub_pinmux.reg'
tc_ub_create_reg_file_comment = 'pinmux'
tc_ub_create_reg_file_start = '20e0000'
tc_ub_create_reg_file_stop = '20e093c'
tc_ub_readreg_mask = '0xffffffff'
tc_ub_create_reg_file_mode = 'w+'
tc_ub_readreg_type = 'l'

tc_ub_create_reg_file_name = 'src/files/fipad_ub_pinmux.reg'
tc_ub_create_reg_file_comment = 'pinmux'
tc_ub_create_reg_file_start = '20e0000'
# for DUTS
tc_ub_memory_ram_ws_base = '0x10000000'
tc_ub_memory_ram_big = 'no'
# uboot_get_parameter_file_list = ['.config', 'include/configs/am335x_shc.h', 'include/configs/ti_armv7_common.h']
tc_ub_i2c_help_with_bus = 'yes'

# Linux
tc_lx_create_reg_file_start = '0x2648000'
tc_lx_create_reg_file_stop = '0x2648178'
tc_lx_readreg_mask = 0xffffffff
tc_lx_readreg_type = 'w'
tc_lx_create_reg_file_name = 'fipad_lx_pinmux.reg'
