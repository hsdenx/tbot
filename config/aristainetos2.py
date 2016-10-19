# tbot configuration
# for the aristainetos board
boardname = 'aristainetos2'
boardlabpowername = 'aristainetos'
boardlabname = 'aristainetos'
boardlabname = 'aristainetos'
tftpboardname = 'aristainetos'
debug=False
debugstatus=True

wdt_timeout = '5000'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

#variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x12000000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
tc_workfd_apply_patchwork_patches_list_hand = [
]

tc_workfd_compile_linux_mkimage = '/home/hs/u-boot/tools/mkimage'

# linux testcases
tc_lab_get_linux_source_git_repo = '/home/hs/abb/imx6/linux'
tc_lab_get_linux_source_git_branch = '20160517-v4.6-rc7'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_get_linux_source_git_repo = 'git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git'
tc_lab_get_linux_source_git_repo = '/home/git/linux.git'
tc_lab_get_linux_source_git_branch = 'master'
tc_lab_get_linux_source_git_branch = 'v4.6'
tc_lab_apply_patches_dir = '/work/hs/tbot/patches/aristainetos2_linux_patches'
tc_lab_toolchain_rev = '5.4'
tc_lab_toolchain_name = 'armv5te'
tc_workfd_compile_linux_clean = 'yes'
tc_workfd_compile_linux_boardname = 'aristainetos2'
tc_workfd_compile_linux_load_addr = '0x10008000'
tc_workfd_compile_linux_modules ='yes'
tc_workfd_compile_linux_modules_path ='/opt/eldk-5.5/armv5te/rootfs-qte-sdk/home/hs/aristaintetos2/modules'
tc_workfd_compile_linux_dt_name = ['imx6dl-aristainetos2_7.dtb', 'imx6dl-aristainetos2_4.dtb']
tc_workfd_compile_linux_fit_its_file = '/work/hs/tbot/files/kernel_fdt_ari2.its'
tc_workfd_compile_linux_fit_file = 'aristainetos2.itb'
tc_workfd_compile_linux_append_dt = 'no'
tc_workfd_compile_linux_makeoptions = '-j8'
tc_lx_create_reg_file_name = 'src/files/aristainetos2_pinmux.reg'
