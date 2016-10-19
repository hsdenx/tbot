# tbot configuration
# for the lab at hs home
# No real lab, power is powered on/off by hand
ip='192.168.178.29'
user='hs'
accept_all=True
keepalivetimeout=1
channel_timeout=0.5

labsshprompt = '$ '
kermit_line = '/dev/ttyUSB1'

tc_workfd_work_dir = '/work/hs/tbot'
lab_tmp_dir = '/var/tmp/'

tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_lab_denx_power_tc = 'tc_lab_interactive_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_interactive_get_power_state.py'
