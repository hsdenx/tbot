# tbot configuration
# for the tqm5200 board
boardname = 'tqm5200'
debug=False
debugstatus=True
loglevel='INFO'
wdt_timeout = '300'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin ts0 tqm5200'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
tftpboardname ='tqm5200s'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x21000000'
tc_ub_boot_linux_load_env = 0
ub_boot_linux_cmd ='run net_nfs'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_boardname = 'TQM5200S'
tc_lab_toolchain_rev = '5.4'
tc_lab_toolchain_name= 'powerpc'
board_has_debugger = 1

tc_ub_memory_ram_ws_base = '0x100000'
tc_ub_memory_ram_ws_base_alt = '0x200000'
tc_ub_memory_ram_big = 'yes'
