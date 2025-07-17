import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from control import ctrl

"""
TODO:
- Bg Colour: white
- App: word, music app, chrome
- Launch on startup
- Hide in system tray
- System message notifying startup

Extension:
- Custom apps
"""

class App(tk.Tk): # Window configuration
    def click(self, button): # TODO: link button clicked to applications
        command = ctrl()
        command.setName(button)
        name = command.getName()
        command.press(name) # TODO: default browser

    def __init__(self):
        super().__init__()

        self.title("App Controller")
        self.geometry("500x400")


        # Heading
        self.label = ttk.Label(self, text="Main Control", font=("Times New Roman", 13))       
        self.label.grid(row=0, column=5)

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
                               command=lambda: self.click("word")
                              )
        self.word.grid(
            column=0,
            row=1,
            padx=5,
            pady=5
        )

        # Chrome
        self.chrome = ttk.Button(self,
                                 image = self.chrome_icon,
                                 command=lambda: self.click("chrome"))
        self.chrome.grid(
            column=1,
            row=1,
            padx=5,
            pady=5
        )
        
        # Music
        self.music = ttk.Button(self,
                                image = self.music_icon,
                                command=lambda: self.click("music"))
        self.music.grid(
            column=2,
            row=1,
            padx=5,
            pady=5
        )

        # FIXME: Temp exit button for testing
        self.exit = ttk.Button(self, text="Exit (This is for test purposes)", command=lambda: self.quit()).grid(column=0, row= 4)

if __name__ == "__main__":
    app = App()
    app.mainloop()