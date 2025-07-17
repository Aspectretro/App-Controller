from AppOpener import open

"""
Overall control of the communication between the buttons to the applications
"""

class ctrl():
    def __init__(self):
        super().__init__()

    def press(self): # TODO: determine which button is pressed
        open("QQ音乐")