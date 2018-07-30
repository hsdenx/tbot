# This file contains default values for all
# variables testcases use ...

debug = False
debugstatus = False
uboot_autoboot_key = ''
state_uboot_timeout = 1
tb_power_state = 'undef'
term_line_length = '200'
wdt_timeout = '120' # wdt timeout after 2 minutes
state_linux_timeout = 4
labsshprompt = '$ '
tc_return = True
ub_boot_linux_cmd = 'run tbot_boot_linux'
do_connect_to_board = True
tftpboardname = 'config.boardname'
boardlabname = 'config.boardname'
boardlabpowername = 'config.boardname'
tftpboardrootdir = ''
tc_lab_toolchain_rev = "5.4"
tc_lab_toolchain_name = "armv5te"
tc_lx_gpio_val = '1'
tc_lab_denx_power_tc = 'tc_lab_denx_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_denx_get_power_state.py'
tc_lab_denx_connect_to_board_tc = 'tc_lab_denx_connect_to_board.py'
tc_lab_denx_disconnect_from_board_tc = 'tc_lab_denx_disconnect_from_board.py'
linux_prompt_default = 'root@generic-armv7a-hf:~# '
labprompt = 'config.linux_prompt'
linux_user = 'root'
create_dot = 'no'
create_statistic = 'no'
create_dashboard = 'no'
create_webpatch = 'no'
create_html_log = 'no'
create_documentation = 'no'
event_documentation_strip_list = []
tb_set_after_linux = ''
