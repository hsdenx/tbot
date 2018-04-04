# the "board" where test run, is the lab PC
# see config_lab_test.py, we use testcase tc_workfd_connect_with_ssh.py
# for connecting to our boards console.
#
# Adapt connect_with_ssh_user to your real username
# on the machine where you have tbot installed.
# we use the same machine as lab PC and as board,
# where the (linux tests only) can be run.
#
# adapt in password-test.py the password (or public key
# file) for your user
#
# and start tbot with:
# tbot.py -s lab_test -c tbot_test -t tc_workfd_date -l log/tbot_pi_test -v -p password-test.py
#
boardname = 'pi'
connect_with_ssh_user = 'hs'
connect_with_ssh_ip = 'localhost'
uboot_prompt = '=> '
linux_prompt = 'ttbott> '
linux_prompt_default = '$ '
debug = False
debugstatus = False
wdt_timeout = '20'
