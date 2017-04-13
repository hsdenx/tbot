class gpo(object):
    path= '/sys/class/gpio/'
    state = None
    def __init__(self, number):
        self.number = str(number)