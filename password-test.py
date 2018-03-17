# passwords for the lab
if (board == 'localhost'):
    if (user == 'pi'):
        password = 'raspberrytbot2go'
    elif (user == 'pi_sudo'):
        password = 'raspberrytbot2go'
    elif (user == 'root'):
        password = 'putherethepasswd'
        print("Please change %s password for user %s\n" % (board, user))
    else:
        print("Please change %s password for user %s\n" % (board, user))
else:
    print("Please change %s password for user %s\n" % (board, user))
