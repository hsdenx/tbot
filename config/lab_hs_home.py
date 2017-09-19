# tbot configuration
# for the lab at hs home
# No real lab, power is powered on/off by hand
ip='192.168.1.105'
user='hs'
accept_all=True
keepalivetimeout=1
channel_timeout=0.5
loglevel = 'INFO'
tftpdir = '/var/lib//tftpboot'
labsshprompt = '$ '
kermit_line = '/dev/ttyUSB1'

tc_workfd_work_dir = '/work/hs/tbot'
lab_tmp_dir = '/var/tmp/'

tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_lab_denx_power_tc = 'tc_lab_interactive_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_interactive_get_power_state.py'

# lab specific changes for my lab
def set_labspecific(tb):
    if tb.config.boardname == 'am335x_evm':
        tb.config.kermit_line = '/dev/ttyUSB0'
        ub_load_board_env_set = [
            'setenv serverip 192.168.2.1',
            'setenv netmask 255.255.255.0',
            'setenv ipaddr 192.168.2.11',
        ]
