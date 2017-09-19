# config file for the beagelboneblack if we boot with
# debian rootfs

linux_prompt_default = '~$ '
linux_user = 'debian'
linux_user_yoctorootfs = 'root'
linux_user_nfsrootfs = linux_user_yoctorootfs
linux_prompt_default_nfsrootfs = '~# '
devmem2_pre = 'sudo /home/debian/'
#tb_set_after_linux = 'tc_board_bbb_after_linux_booted.py'

# load common settings
config_list = ['beagleboneblack']
