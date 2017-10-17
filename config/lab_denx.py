# tbot configuration
# for the denx vlab
ip = 'pollux.denx.org'
user = 'hs'
accept_all = True
keepalivetimeout = 1
channel_timeout = 0.5
loglevel = 'INFO'
wdt_timeout = '900'

tc_workfd_work_dir = '/work/hs/tbot/'
lab_tmp_dir = '/var/tmp/'
tftpdir = '/tftpboot/'

# lab specific changes for the mbconnect lab
def set_labspecific(tb):
    if tb.config.boardname == 'am335x_evm':
        tb.config.tc_ub_boot_linux_load_env = 'set'
	tb.config.ub_load_board_env_set = [
		'setenv serverip 192.168.1.1',
		'setenv netmask 255.255.0.0',
		'setenv ipaddr 192.168.20.95',
		]
	tb.config.boardlabname = 'bbb'
	tb.config.tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
	tb.config.tftpboardname = 'bbb'
	tb.config.boardlabpowername = 'bbb'
        # older u-boot version have this prompt
        # tb.config.uboot_prompt = 'U-Boot# '
        # after updating to newer version uncomment this
        tb.config.tc_demo_compile_install_test_name = 'tc_demo_uboot_tests.py'
        tb.config.tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
        tb.config.tc_workfd_connect_with_kermit_rlogin = 'rlogin metis bbb'
        tb.config.tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'
        tb.config.tc_board_bootmode_tc = 'tc_board_bbb_bootmode_labdenx.py'
