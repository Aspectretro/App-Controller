import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

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
    def click(self):
        print("Clicked")

    def __init__(self):
        super().__init__()

        self.title("App Controller")
        self.geometry("500x400")

        # Heading
        self.label = ttk.Label(self, text="Main Control", font=("Times New Roman", 13))       
        self.label.pack()

        # Image
        originalWord = Image.open("./assets/Word.png")
        originalChrome = Image.open("./assets/Chrome.png")
        originalMusic = Image.open("./assets/Music.png")

        resizeWord = originalWord.resize((50,50), Image.LANCZOS)
        resizeChrome = originalChrome.resize((50,50), Image.LANCZOS)
        resizeMusic = originalMusic.resize((50,50), Image.LANCZOS)

        # Icon
        self.word_icon = ImageTk.PhotoImage(resizeWord)
        self.chrome_icon = ImageTk.PhotoImage(resizeChrome)
        self.music_icon = ImageTk.PhotoImage(resizeMusic)

        # Word
        self.word = ttk.Button(self, 
                               image=self.word_icon, 
                               command=self.click)
        self.word.pack(
            ipadx=5,
            ipady=5,
        )

        # Chrome
        self.chrome = ttk.Button(self,
                                 image = self.chrome_icon,
                                 command = self.click)
        self.chrome.pack(
            ipadx=5,
            ipady=5
        )
        
        # Music
        self.music = ttk.Button(self,
                                image = self.music_icon,
                                command = self.click)
        self.music.pack(
            ipadx=5,
            ipady=5
        )

if __name__ == "__main__":
    app = App()
    app.mainloop()
