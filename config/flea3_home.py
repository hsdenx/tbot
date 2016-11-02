# tbot configuration
# for the flea3 board at home (no automated power on/off)
# yet, so switch the power state manually
boardname = 'flea3'
tftpboardname = 'flea3'
debug = False
debugstatus = True
ip = '192.168.178.29'
user = 'hs'
accept_all = True
keepalivetimeout = 1
channel_timeout = 0.5
loglevel ='INFO'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

labsshprompt = '$ '
kermit_line = '/dev/ttyUSB1'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'

tc_lab_denx_power_tc = 'tc_lab_interactive_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_interactive_get_power_state.py'

# enable some event handlers
#create_dot = 'yes'
#create_statistic = 'yes'
#create_dashboard = 'yes'
#webpatch = 'yes'

# variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'

tc_workfd_generate_random_file_name = '/var/lib/tftpboot/flea3/tbot/nor_random'
tc_workfd_generate_random_file_length = '128k'
