# tbot configuration
# for the testing fast a tbot installation
# No real lab, power is powered on/off by hand
#
ip = 'localhost'
user = 'config.connect_with_ssh_user'
accept_all = True
keepalivetimeout = 1
channel_timeout = 0.5
loglevel = 'INFO'
lab_tmp_dir = '/var/tmp'

tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_ssh.py'
tc_lab_denx_power_tc = 'tc_lab_interactive_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_interactive_get_power_state.py'
