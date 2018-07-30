# tbot configuration
# for the sigmatek-nand board
# special usecase, check all U-Boot patches
# at patchwork
boardname = 'sigmatek-nand'
debug=False
debugstatus=True
loglevel='INFO'
wdt_timeout = '5000'
state_linux_timeout = '8'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '
linux_prompt_default = 'sigmatek-arm:'

tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x11000000'
