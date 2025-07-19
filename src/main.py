import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from control import ctrl


class App(tk.Tk): # Window configuration
    def __init__(self):
        super().__init__()
        self.command = ctrl()
        self.title("App Controller")
        self.geometry("500x400")

        # Grid confgiure
        for i in range(5): # 5 icon per row
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(i, weight=1)

        # Heading
        self.label = ttk.Label(self, text="Main Control", font=("Times New Roman", 13))       
        self.label.grid(row=0, column=3, sticky="nsew")

        # Image
        self.icons = {}
        apps = ["Word", "Chrome", "File", "Music", "Settings"]
        for app in apps:
            try:
                img = Image.open(f"./assets/{app}.png")
                img = img.resize((50, 50), Image.LANCZOS)
                self.icons[app.lower()] = ImageTk.PhotoImage(img)
            except Exception:
                print(f"failed to load {app} icon")

        # Buttons
        buttons = [
            ("word", 0, lambda: self.click("word")),
            ("chrome", 1, self.browser),
            ("music", 2, lambda: self.click("qq music")),
            ("file", 3, lambda: self.click("file explorer")),
            ("settings", 4, lambda: self.click("settings"))
        ]
        for name, col, cmd in buttons:
            icon = self.icons.get(name)
            btn = ttk.Button(self, image=icon, command=cmd)
            if not icon:
                btn.config(text=name.capitalize())
            btn.grid(column=col, row=1, padx= 5, pady=5, sticky="nsew")
        

        # FIXME: Temp exit button for testing
        self.exit = ttk.Button(self, text="Exit", command=lambda: self.quit()).grid(column=0, row= 4)

    def browser(self): # This is for browser ONLY
        browser_name = self.command.get_default_browser_windows()
        print(browser_name)
        self.command.press(browser_name)
    
    def click(self, name):
        try:
            self.command.press(name.lower())
        except Exception:
            messagebox.showerror(f'Failed to load {name}')

if __name__ == "__main__":
    app = App()
    app.mainloop()




# originalWord = Image.open("./assets/Word.png")
#         originalChrome = Image.open("./assets/Chrome.png")
#         originalMusic = Image.open("./assets/Music.png")
#         originalFile = Image.open("./assets/File.png") 
#         originalSetting = Image.open("./assets/Settings.png")

#         resizeWord = originalWord.resize((50,50), Image.LANCZOS)
#         resizeChrome = originalChrome.resize((50,50), Image.LANCZOS)
#         resizeMusic = originalMusic.resize((50,50), Image.LANCZOS)
#         resizeFile = originalFile.resize((50,50), Image.LANCZOS)
#         resizeSetting = originalSetting.resize((50,50), Image.LANCZOS)

#         # Icon
#         self.word_icon = ImageTk.PhotoImage(resizeWord)
#         self.chrome_icon = ImageTk.PhotoImage(resizeChrome)
#         self.music_icon = ImageTk.PhotoImage(resizeMusic)
#         self.file_icon = ImageTk.PhotoImage(resizeFile)
#         self.setting_icon = ImageTk.PhotoImage(resizeSetting)

#         # Word
#         self.word = ttk.Button(self, 
#                                image=self.word_icon, 
#                                command = lambda: self.click("word")
#                               )
#         self.word.grid(
#             column=0,
#             row=1,
#             padx=5,
#             pady=5
#         )

#         # Chrome
#         self.chrome = ttk.Button(self,
#                                  image = self.chrome_icon,
#                                  command = self.browser
#                                  )
#         self.chrome.grid(
#             column=1,
#             row=1,
#             padx=5,
#             pady=5
#         )
        
#         # Music
#         self.music = ttk.Button(self,
#                                 image = self.music_icon,
#                                 command = lambda: self.click("music")
#                                 )
#         self.music.grid(
#             column=2,
#             row=1,
#             padx=5,
#             pady=5
#         )

#         # File Explorer
#         self.file = ttk.Button(self,
#                                image = self.file_icon,
#                                command = lambda: self.click("file explorer")
#                                )
        
#         self.file.grid(
#             column=3,
#             row=1,
#             padx=5,
#             pady=5
#         )

#         # Setting
#         self.settings = ttk.Button(self, 
#                                    image = self.setting_icon, 
#                                    command=lambda: self.click("settings")
#                                    )
#         self.settings.grid(
#             column=4,
#             row=1,
#             padx=5,
#             pady=5
#         )