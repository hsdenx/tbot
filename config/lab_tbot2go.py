# tbot configuration for the tbot2go lab
from gpio import gpo

ip='192.168.3.1' # lab pc ip
user='pi' # lab pc user
accept_all=True
keepalivetimeout=2
channel_timeout=1
loglevel = 'INFO'
lab_tmp_dir = '/var/tmp'

labsshprompt = '$ ' # first prompt after logging into lab pc via ssh

gpio_power_on = gpo(4) # gpio number of gpio used to controll power of board
jumper = gpo(2)
kermit_line = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0'

tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_lab_denx_power_tc = 'tc_lab_power_onoff_gpio.py'
tc_lab_denx_get_power_state_tc = 'tc_dummy.py'

compile_pc_ip = '192.168.3.10'
compile_pc_user= 'hs'
compile_pc_prompt = 'ttbott_compile> '
connect_to_compilepc_ssh_opt = ''
connect_to_compilepc_ssh_cmd_prompt = '$ '

state_linux_timeout = 6

tftpdir = '/srv/tftpboot/'
tc_lab_source_dir = '/work/tbot2go/tbot/'
tc_workfd_work_dir = '/work/tbot2go/tbot/'

tc_lab_prepare_tc_name = 'tc_lab_prepare_tbot2go.py'

tc_workfd_iperf_minval = 40

# lab specific changes for the tbot2go lab
def set_labspecific(tb):
    if tb.config.boardname == 'cuby':
        tb.config.state_linux_timeout = 4
        tb.config.yocto_results_dir = '$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/'
        tb.config.yocto_results_dir_lab = tb.config.tc_board_cuby_yocto_result_dir
        tb.config.nfs_subdir = tb.config.tc_board_cuby_nfs_dir_w
        tb.config.gpio_power_on = gpo(12) # gpio number of gpio used to controll power of board
        tb.config.kermit_line = '/dev/serial/by-id/usb-FTDI_FT4232H_Device_FTYY8G4Q-if00-port0'

