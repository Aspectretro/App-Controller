import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from control import ctrl

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.command = ctrl()
        self.title("App Controller")
        self.geometry("500x400")
        
        # Main container frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Load icons
        self.icons = {}
        apps = ["Word", "Chrome", "File", "Music", "Settings", "Lightroom", "Logseq"]
        for app in apps:
            try:
                img = Image.open(f"./assets/{app}.png")
                img = img.resize((50, 50), Image.LANCZOS)
                self.icons[app.lower()] = ImageTk.PhotoImage(img)
            except Exception:
                print(f"Failed to load {app} icon")

        # Button configuration
        buttons = [
            ("word", lambda: self.click("word")),
            ("chrome", lambda: self.click("google chrome")),
            ("music", lambda: self.click("qq music")),
            ("file", lambda: self.click("file explorer")),
            ("settings", lambda: self.click("settings")),
            ("lightroom", lambda: self.click("adobe lightroom")),
            ("logseq", lambda: self.click("logseq"))
        ]
        
        # Calculate grid dimensions
        cols_per_row = 5  # Maximum buttons per row
        total_buttons = len(buttons)
        rows = (total_buttons + cols_per_row - 1) // cols_per_row
        
        # Configure grid weights
        for r in range(rows):
            self.main_frame.grid_rowconfigure(r, weight=1)
        for c in range(cols_per_row):
            self.main_frame.grid_columnconfigure(c, weight=1)
        
        # Place buttons in grid
        for index, (name, cmd) in enumerate(buttons):
            row = index // cols_per_row
            col = index % cols_per_row
            
            icon = self.icons.get(name)
            btn = ttk.Button(
                self.main_frame, 
                image=icon, 
                command=cmd,
                compound=tk.TOP  # Show text below icon if both exist
            )
            
            if not icon:
                btn.config(text=name.capitalize())
                
            btn.grid(
                row=row, 
                column=col, 
                padx=5, 
                pady=5, 
                sticky="nsew"
            )
        
        # Exit button at bottom
        exit_frame = ttk.Frame(self)
        exit_frame.pack(fill="x", padx=10, pady=10)
        ttk.Button(
            exit_frame, 
            text="Exit", 
            command=self.quit
        ).pack(side="right")
    
    def click(self, name):
        try:
            self.command.press(name.lower())
        except Exception:
            messagebox.showerror("Error", f'Failed to load {name}')

if __name__ == "__main__":
    app = App()
    app.mainloop()