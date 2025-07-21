from AppOpener import open
import webbrowser

class ctrl():
    def __init__(self):
        self.name = None
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def press(self, name): # TODO: obtain information from os to find default browser
        if not name:
            return False
        else:
            open(name.lower())