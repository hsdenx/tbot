# tbot configuration
# for the lab at hs home
ip='192.168.178.29'
user='hs'
accept_all=True
keepalivetimeout=1
channel_timeout=0.5
loglevel = 'INFO'

labsshprompt = '$ '

tc_workfd_work_dir = '/work/hs/tbot'
lab_tmp_dir = '/var/tmp/'
tftprootdir = '/var/lib/tftpboot/'

tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_lab_denx_power_tc = 'tc_lab_sispmctl_set_power_state.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_sispmctl_get_power_state.py'
