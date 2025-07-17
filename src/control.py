from AppOpener import open
import os
import winreg

"""
Overall control of the communication between the buttons to the applications
"""

class ctrl():
    def __init__(self):
        super().__init__()
    
    def get_default_browser_windows():
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                            r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
                browser = winreg.QueryValueEx(key, 'ProgId')[0]
                return browser
        except Exception as e:
            print(f"Error accessing registry: {e}")
            return None
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def press(self, name): # TODO: obtain information from os to find default browser
        default_browser = self.get_default_browser_windows()
        if name.lower() == default_browser:
            open(default_browser)
        elif name.lower() == "word":
            open("word")
        elif name.lower() == "music":
            open("QQ音乐")