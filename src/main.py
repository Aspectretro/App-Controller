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
        # TODO: open web applications, more applications
        buttons = [
            ("word", 0, lambda: self.click("word")),
            ("chrome", 1, lambda: self.click("google chrome")),
            ("music", 2, lambda: self.click("qq music")),
            ("file", 3, lambda: self.click("file explorer")),
            ("settings", 4, lambda: self.click("settings")),
            ("", 5, lambda: self.click(""))
        ]
        for name, col, cmd in buttons:
            icon = self.icons.get(name)
            btn = ttk.Button(self, image=icon, command=cmd)
            if not icon:
                btn.config(text=name.capitalize())
            btn.grid(column=col, row=1, padx= 5, pady=5, sticky="nsew")
        

        # FIXME: Temp exit button for testing
        self.exit = ttk.Button(self, text="Exit", command=lambda: self.quit()).grid(column=0, row= 4)
    
    def click(self, name):
        try:
            self.command.press(name.lower())
        except Exception:
            messagebox.showerror(f'Failed to load {name}')

if __name__ == "__main__":
    app = App()
    app.mainloop()