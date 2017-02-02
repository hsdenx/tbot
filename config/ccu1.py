# tbot configuration
# for the ccu1 board
boardname = 'ccu1'
debug=False
debugstatus=True
loglevel='INFO'

uboot_prompt = 'OMAP3 usbc # '
linux_prompt = 'ttbott> '

# variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'
tc_ub_boot_linux_load_env = 'no'
ub_boot_linux_cmd='run net_nfs_self'

tc_lx_mount_dev = '/dev/mmcblk0p2'
tc_lx_bonnie_sz = '512'

tc_lx_create_reg_file_name = 'src/files/ccu1_pinmux_scm.reg'
tc_lx_create_reg_file_start = '0x48002030'
tc_lx_create_reg_file_stop = '0x48002530'
tc_lx_readreg_mask = '0xffffffff'

# gpmc
# self.tc_lx_create_reg_file_name = 'src/files/ccu1_pinmux_gpmc.reg'
# self.tc_lx_create_reg_file_start = '0x6e000000'
# self.tc_lx_create_reg_file_stop = '0x6e000300'
