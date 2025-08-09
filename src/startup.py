import sys
import os
import winreg as reg
import platform
from pathlib import Path

class Startup:
    def __init__(self, name):
        self.name = name
        self.platform = platform.system()

    def enable_start(self):
        if self.platform == "Windows":
            self.enable_windows()
        else:
            pass

    def disable_start(self):
        if self.platform == "Windows":
            self.disable_windows()
        else:
            pass
    
    def enable_windows(self):
        key = reg.HKEY_CURRENT_USER
        keyPath = r"Software\Microsoft\Windows\CurrentVersion\Run"

        try:
            with reg.OpenKey(key, keyPath, 0, reg.KEY_SET_VALUE) as register:
                reg.SetValueEx(
                    register,
                    self.name,
                    reg.REG_SZ,
                    self.get_path()
                )
        
        except Exception as e:
            print(f"failed to load: {e}")

    def disable_windows(self):
        key = reg.HKEY_CURRENT_USER
        keyPath = r"Software\Microsoft\Windows\CurrentVersion\Run"

        try:
            with reg.OpenKey(key, keyPath, 0, reg.KEY_SET_VALUE) as register:
                reg.DeleteValue(register, self.name)
        
        except WindowsError:
            pass

    def is_enabled(self): # check if it is enabled
        if self.platform == "Windows":
            return self.check_windows()
        return False

    def check_windows(self): # check registry on startup
        key = reg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        try:
            with reg.OpenKey(key, key_path) as registry_key:
                value, _ = reg.QueryValueEx(registry_key, self.name)
                return value == self.get_path()
        except WindowsError:
            return False

    def get_path(self):
        if getattr(sys, "frozen", False):
            return sys.executable
        return f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}"'