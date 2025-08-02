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

        # config window grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame
        self.set_frame = ttk.Frame(self)
        self.set_frame.pack(expand=True, fill="both", padx=5, pady=5)

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
        
        # Set constant
        button_size = 100 # size of each square button
        cols_row = 4 # number of buttons per row

        # Find dimension
        for r in range(len(buttons) + cols_row - 1) // cols_row:
            self.set_frame.grid_rowconfigure(r, weight=1, minsize=button_size)
        for c in range(cols_row):
            self.set_frame.grid_columnconfigure(c, weight=1, minsize=button_size)

        # Image
        self.icons = {}
        for name, _ in buttons:
            try:
                img = Image.open(f"./assets/{app}.png")
                img = img.resize((button_size - 20, button_size - 20), Image.LANCZOS)
                self.icons[name] = ImageTk.PhotoImage(img)
            except Exception:
                print(f"failed to load {app} icon")
                self.icons[name] = None

        # Placing buttons
        self.btnWidgets = []
        for index, (name, cmd) in enumerate(buttons):
            rows = index // cols_row
            col = index % cols_row

            icon = self.icons.get(name)
            btn = ttk.Button(
                self.set_frame,
                image=icon,
                command=cmd,
                compound=tk.TOP
            )

            # button config
            btn.config(
                width=button_size,
                height=button_size,
                anchor="center"
            )

            btn.grid(
                row=rows,
                column=col,
                padx=5,
                pady=5,
                sticky="nesw"
            )
            self.btnWidgets.append(btn)
        

        # FIXME: Temp exit button for testing
        exitBtn = ttk.Frame(self)
        exitBtn.pack(fill='x', padx=10, pady=10)
        ttk.Button(
            exitBtn,
            text="Exit",
            command=self.quit
        ).pack(side="right")

        self.bind("<Configure", self.window_resize)

    def window_resize(self, event):
        width = self.winfo_width()
        height = self.winfo_height()

        cols = 4
        rows = (len(self.btnWidgets) + cols - 1) // cols
        btnSize = min(
            (width - 40) // cols,
            (height - 80) // rows
        )

        for btn in self.btnWidgets:
            btn.config(width=btnSize, height=btnSize)

            if btn["image"]:
                imgName = btn['text'].lower() if btn['text'] else ""
                if imgName in self.icons:
                    try:
                        original_img = Image.open(f"./assets/{imgName}.png")
                        new_size = btnSize - 20  # Padding
                        resized_img = original_img.resize((new_size, new_size), Image.LANCZOS)
                        new_photo = ImageTk.PhotoImage(resized_img)
                        btn.config(image=new_photo)
                        btn.image = new_photo
                    except Exception:
                        print("An error occured. Please debug")  # Keep reference
    
    def click(self, name):
        try:
            self.command.press(name.lower())
        except Exception:
            messagebox.showerror(f'Failed to load {name}')

if __name__ == "__main__":
    app = App()
    app.mainloop()