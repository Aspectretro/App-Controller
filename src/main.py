import tkinter as tk
from tkinter import ttk
import os

"""
Planning:
- Bg Colour:
- App:
- Launch on startup
- Hide in system tray
- System message notifying startup

Extension:
- Custom apps
- Custom bg
"""

class App(tk.Tk): # Window configuration
    def __init__(self):
        super().__init__()

        self.title("App Controller")
        self.geometry("500x400")

        self.label = ttk.Label(self, text="Main Control", font=("Times New Roman", 13))       
        self.label.pack()


        # Font configure

if __name__ == "__main__":
    app = App()
    app.mainloop()
