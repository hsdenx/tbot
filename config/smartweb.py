# tbot configuration
# for the smartweb board
boardname = 'smartweb'
tftpboardname = 'smartweb_hw'
debug = False
debugstatus = True

uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin ts3 smartweb'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x21000000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'

tc_workfd_apply_patchwork_patches_list_hand = [
	'627922', # [U-Boot,1/7] mtd: nand: Remove jz4740 driver
	'627924', # [U-Boot,2/7] mtd: nand: Remove docg4 driver and palmtreo680 flashing tool
	'627923', # [U-Boot,3/7] mtd: nand: Remove nand_info_t typedef
	'627925', # [U-Boot,4/7] nand: Embed mtd_info in struct nand_chip
	'627926', # [U-Boot,5/7] mtd: nand: Add+use mtd_to/from_nand and nand_get/set_controller_data
	'627927', # [U-Boot,6/7] mtd: nand: Add page argument to write_page() etc.
	'627928', # [U-Boot,7/7] mtd: nand: Sync with Linux v4.6
]
tc_workfd_apply_patchwork_patches_blacklist = ['204183', '561384']

uboot_get_parameter_file_list = ['.config', 'include/configs/smartweb.h', 'arch/arm/mach-at91/include/mach/at91sam9260.h']
