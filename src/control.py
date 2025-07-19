from AppOpener import open
import webbrowser
import winreg

class ctrl():
    def __init__(self):
        self.name = None
        self.browser_id = {
            "ChromeHTML": "google chrome",
            "MSEdgeHTM": "microsoft edge",
            "FirefoxURL": "firefox",
            "OperaStable": "opera gx browser",
        }
    
    def get_default_browser_windows(self) -> str:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                            r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
                browser = winreg.QueryValueEx(key, 'ProgId')[0]
                return self.browser_map.get(browser) 
        except Exception:
            return None


    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def press(self, name): # TODO: obtain information from os to find default browser
        if not name:
            return False
        try:
            if name.lower() in ["google chrome", "microsoft edge", "firefox", "opera gx browser"]:
                default_brower = self.get_default_browser_windows()
                open(default_brower)
            else:
                open(name.lower())
        except Exception as e:
            print(f"Error opening application '{name}': {e}")
            if "browser" in name.lower():
                webbrowser.open("about: blank")