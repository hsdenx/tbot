# tbot configuration
# for the flea3 board
boardname = 'flea3'
tftpboardname = 'flea3'
debug=False
debugstatus=True
loglevel='INFO'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

# variables used in testcases
tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'

tc_workfd_generate_random_file_name = '/tftpboot/flea3/tbot/nor_random'
tc_workfd_generate_random_file_length = '128k'
