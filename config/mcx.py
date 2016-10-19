# tbot configuration
# for the mcx board
boardname = 'mcx'
debug=False
debugstatus=True
loglevel='INFO'
wdt_timeout = '5000'

uboot_prompt = 'mcx # '
linux_prompt = 'ttbott> '

# variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'

linux_prompt_default = 'root@generic-armv5te:~#'

tc_lx_mount_dev = '/dev/mmcblk0p2'
tc_lx_bonnie_sz = '512'

tc_lx_create_reg_file_name = 'src/files/mcx_pinmux.reg'
tc_lx_create_reg_file_start = '0x48002030'
tc_lx_create_reg_file_stop = '0x48002264'
tc_lx_readreg_mask = 0xffffffff
tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/mcx_linux_ml_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'

