from AppOpener import open
import os
import winreg

"""
Overall control of the communication between the buttons to the applications
"""

class ctrl():
    def __init__(self):
        super().__init__()
    
    def get_default_browser_windows(self) -> str:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                            r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
                browser = winreg.QueryValueEx(key, 'ProgId')[0]
                return self.browser_map(browser) 
        except Exception as e:
            print(f"Error accessing registry: {e}")
            return None
    def browser_map(self, prog_id):
        """
        Since google chrome is being used world wide as the number one default browser with a 64%
        global usage, the default assumption of browser setting will be chrome.
        """
        browser_id = {
            "ChromeHTML": "google chrome",
            "MSEdgeHTM": "microsoft edge",
            "FirefoxURL": "firefox",
            "OperaStable": "opera",
        }
        return browser_id.get(prog_id, "chrome")

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def press(self, name): # TODO: obtain information from os to find default browser
        app_name = name.lower() if name else self.getName().lower()
        try:
            if app_name == self.get_default_browser_windows().lower():
                open(self.get_default_browser_windows())
            else:
                open(app_name)
        except Exception as e:
            print(f"Error opening application '{app_name}': {e}")
            