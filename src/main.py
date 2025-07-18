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
    def __init__(self):
        super().__init__()
        self.command = ctrl()

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
                               command = lambda: self.click("word")
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
                                 command = self.browser()
                                 )
        self.chrome.grid(
            column=1,
            row=1,
            padx=5,
            pady=5
        )
        
        # Music
        self.music = ttk.Button(self,
                                image = self.music_icon,
                                command = lambda: self.click("music")
                                )
        self.music.grid(
            column=2,
            row=1,
            padx=5,
            pady=5
        )

        # FIXME: Temp exit button for testing
        self.exit = ttk.Button(self, text="Exit", command=lambda: self.quit()).grid(column=0, row= 4)

    def browser(self): # This is for browser ONLY
        command = ctrl()
        name = command.get_default_browser_windows()
        command.press(name) # TODO: default browser
    
    def click(self, name):
        command = ctrl()
        command.setName(name)
        app_name = command.getName()
        command.press(app_name)


if __name__ == "__main__":
    app = App()
    app.mainloop()