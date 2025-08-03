import pystray
from PIL import Image
import tkinter as tk

class TrayManage:
    def __init__(self, main_app, icon_path = "assets/layers.png"):
        self.main = main_app
        self.icon = icon_path
        self.tray_icon = None
        self.enabled = True

    def create_icon(self):
        image = Image.open(self.icon)
        menu = pystray.Menu(
            pystray.MenuItem("Open", self.restore),
            pystray.MenuItem("Close", self.quit_app)
        )

        self.tray_icon = pystray.Icon(
            "app_tray_icon",
            image,
            "App Controller",
            menu
        )

    def min_to_tray(self):
        if not self.enabled:
            return
        
        self.main.withdraw()
        if not self.tray_icon:
            self.create_icon()
        self.tray_icon.run()
    
    def restore(self, icon=None, item=None):
        self.main.deiconify()
        self.main.lift()
        if self.tray_icon:
            self.tray_icon.stop()
            self.tray_icon = None

    def quit_app(self, icon=None, item=None):
        if self.tray_icon:
            self.tray_icon.stop()
        self.main.destroy()
    
    def set_tray(self, enabled):
        self.enabled = enabled
        if not enabled and self.tray_icon:
            self.tray_icon.stop()
            self.tray_icon = None