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

        # Frame
        self.set_frame = ttk.Frame(self)
        self.set_frame.pack(expand=True, fill="both", padx=5, pady=5)

        # Image
        self.icons = {}
        apps = ["Word", "Chrome", "File", "Music", "Settings", "Lightroom", "Logseq"]
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
            ("word", lambda: self.click("word")),
            ("chrome", lambda: self.click("google chrome")),
            ("music", lambda: self.click("qq music")),
            ("file", lambda: self.click("file explorer")),
            ("settings", lambda: self.click("settings")),
            ("lightroom", lambda: self.click("adobe lightroom")),
            ("logseq", lambda: self.click("logseq")),
        ]

        # Find dimension
        cols_row = 5
        total_button = len(buttons)
        rows = (total_button + cols_row - 1) // cols_row

        for r in range(rows):
            self.set_frame.grid_rowconfigure(r, weight=1)
        for c in range(cols_row):
            self.set_frame.grid_columnconfigure(c, weight=1)
        
        # Placing buttons
        for index, (name, cmd) in enumerate(buttons):
            rows = index // cols_row
            col = index % cols_row

            icon = self.icons.get(name)
            btn = ttk.Button(
                self.frame,
                image=icon,
                command=cmd
            )
        
            if not icon:
                btn.config(text=name.capitalize())

            btn.grid(
                row=rows,
                column=col,
                padx=5,
                pady=5,
                sticky="nesw"
            )
        

        # FIXME: Temp exit button for testing
        exitBtn = ttk.Frame(self)
        exitBtn.pack(fill='x', padx=10, pady=10)
        ttk.Button(
            exitBtn,
            text="Exit",
            command=self.quit
        ).pack(side="right")
    
    def click(self, name):
        try:
            self.command.press(name.lower())
        except Exception:
            messagebox.showerror(f'Failed to load {name}')

if __name__ == "__main__":
    app = App()
    app.mainloop()