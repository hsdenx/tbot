# config file for the beagelboneblack if we boot with
# yocto rootfs

linux_prompt_default = '~# '
linux_user = 'root'
linux_user_yoctorootfs = 'root'
linux_user_nfsrootfs = linux_user_yoctorootfs
linux_prompt_default_nfsrootfs = '~# '

tc_lx_dmesg_grep_options = ''

# load common settings
config_list = ['beagleboneblack']
