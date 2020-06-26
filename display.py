class Display:
    def __init__(self, model, size):
        self.model = model
        self.size = size

    def show(self, message):
        print "Computer says: " + message + ';'
