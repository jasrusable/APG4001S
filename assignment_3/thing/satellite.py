

class Satellite(object):
    def __init__(self, prn):
        self.prn = prn
        self.epochs = []
        self.observations = []
