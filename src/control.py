from AppOpener import open

"""
Overall control of the communication between the buttons to the applications
"""

class ctrl():
    def __init__(self):
        super().__init__()
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def press(self, name):
        if name.lower() == "chrome":
            open("google chrome")
        elif name.lower() == "word":
            open("word")
        elif name.lower() == "music":
            open("QQ音乐")