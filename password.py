# passwords for the lab
if (board == 'lab'):
    if (user == 'hs'):
        password = 'putherethepasswd'
        print("Please change %s password for user %s\n" % (board, user))
    elif (user == 'root'):
        password = 'putherethepasswd'
        print("Please change %s password for user %s\n" % (board, user))
elif (board == 'pollux.denx.org'):
    if (user == 'hs'):
        print("Please change %s password for user %s\n" % (board, user))
        password = 'putherethepasswd'
# passwords for the boards
elif (board == 'localhost'):
    if (user == 'hs'):
        password = 'DEINPASSWORD'
elif (board == 'am335x_evm'):
    if (user == 'debian'):
        password = 'temppwd'
