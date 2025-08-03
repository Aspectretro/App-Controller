import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from control import ctrl  # Assuming this contains your application control logic
from systemTray import TrayManage
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.command = ctrl()
        
        # Fixed button and window configuration
        self.button_size = 100  # pixels  # window padding
        self.padding = 1
        self.buttons_per_row = 4
        
        # Calculate optimal window size
        num_buttons = len(["Word", "Chrome", "File", "Music", 
                          "Settings", "Lightroom", "Logseq"])
        rows = (num_buttons + self.buttons_per_row - 1) // self.buttons_per_row
        
        window_width = (self.button_size * self.buttons_per_row + 80)  # +20 for scrollbar space
        window_height = (self.button_size * self.buttons_per_row + 60)  # +60 for title bar and exit button
        
        # Window setup
        self.title("App Controller")
        self.geometry(f"{window_width}x{window_height}")
        self.minsize(window_width, window_height)  # Prevent making window too small

        # System Tray Setup
        self.trayManage = TrayManage(self)
        self.create_tray()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Main container with canvas and scrollbar
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Load icons and create buttons
        self.load_icons()
        self.create_buttons()
    
    def create_tray(self):
        settings = ttk.LabelFrame(self, text="Settings")
        settings.pack(fill='x', padx=10, pady=10)

        self.tray_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            settings,
            text="Minimise to system tray when closed",
            variable=self.tray_var,
            command=self.toggle_tray
        ).pack(anchor="w")

    def toggle_tray(self):
        self.trayManage.set_tray(self.tray_var.get())
    
    def on_close(self):
        if self.tray_var.get():
            self.trayManage.min_to_tray()
        else:
            self.destroy()

    def load_icons(self):
        """Load all icons at fixed size"""
        self.icons = {}
        app_names = ["Word", "Chrome", "File", "Music", 
                    "Settings", "Lightroom", "Logseq",
                    "Discord", "zoom"]
        icon_size = self.button_size - 20  # 20px padding
        
        for name in app_names:
            try:
                img = Image.open(f"./assets/{name}.png")
                img = img.resize((icon_size, icon_size), Image.LANCZOS)
                self.icons[name.lower()] = ImageTk.PhotoImage(img)
            except Exception:
                print(f"Failed to load {name} icon")
                self.icons[name.lower()] = None
    
    def create_buttons(self):
        """Create buttons with fixed square size and commands"""
        app_data = [
            ("word", "Word"),
            ("chrome", "Chrome"),
            ("music", "Music"),
            ("file", "File"),
            ("settings", "Settings"),
            ("lightroom", "Lightroom"),
            ("logseq", "Logseq"),
            ('discord', "Discord"),
            ("zoom", "zoom")
        ]
        
        for index, (command_key, display_name) in enumerate(app_data):
            row = index // self.buttons_per_row
            col = index % self.buttons_per_row
            
            btn = tk.Button(
                self.scrollable_frame,
                image=self.icons.get(command_key),
                text=display_name if not self.icons.get(command_key) else "",
                compound=tk.TOP,
                width=self.button_size,
                height=self.button_size,
                borderwidth=0,
                command=lambda key=command_key: self.command.press(key)
            )
            
            btn.grid(
                row=row, 
                column=col, 
                padx=5, 
                pady=5,
                sticky=""
            )
            
            # Configure grid to center content
            self.scrollable_frame.grid_columnconfigure(col, weight=1)
            self.scrollable_frame.grid_rowconfigure(row, weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
# from control import ctrl

# class App(tk.Tk): # Window configuration
#     def __init__(self):
#         super().__init__()
#         self.command = ctrl()
#         self.title("App Controller")
#         self.geometry("500x400")

#         # config window grid
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)

#         # Frame
#         self.set_frame = ttk.Frame(self)
#         self.set_frame.pack(expand=True, fill="both", padx=5, pady=5)

#         # TODO: open web applications, more applications
#         buttons = [
#             ("word", lambda: self.click("word")),
#             ("chrome", lambda: self.click("google chrome")),
#             ("music", lambda: self.click("qq music")),
#             ("file", lambda: self.click("file explorer")),
#             ("settings", lambda: self.click("settings")),
#             ("lightroom", lambda: self.click("adobe lightroom")),
#             ("logseq", lambda: self.click("logseq")),
#         ]
        
#         # Set constant
#         button_size = 100 # size of each square button
#         cols_row = 4 # number of buttons per row

#         # Find dimension
#         for r in range(len(buttons) + cols_row - 1) // cols_row:
#             self.set_frame.grid_rowconfigure(r, weight=1, minsize=button_size)
#         for c in range(cols_row):
#             self.set_frame.grid_columnconfigure(c, weight=1, minsize=button_size)

#         # Image
#         self.icons = {}
#         for name, _ in buttons:
#             try:
#                 img = Image.open(f"./assets/{app}.png")
#                 img = img.resize((button_size - 20, button_size - 20), Image.LANCZOS)
#                 self.icons[name] = ImageTk.PhotoImage(img)
#             except Exception:
#                 print(f"failed to load {app} icon")
#                 self.icons[name] = None

#         # Placing buttons
#         self.btnWidgets = []
#         for index, (name, cmd) in enumerate(buttons):
#             rows = index // cols_row
#             col = index % cols_row

#             icon = self.icons.get(name)
#             btn = ttk.Button(
#                 self.set_frame,
#                 image=icon,
#                 command=cmd,
#                 compound=tk.TOP
#             )

#             # button config
#             btn.config(
#                 width=button_size,
#                 height=button_size,
#                 anchor="center"
#             )

#             btn.grid(
#                 row=rows,
#                 column=col,
#                 padx=5,
#                 pady=5,
#                 sticky="nesw"
#             )
#             self.btnWidgets.append(btn)
        

#         # FIXME: Temp exit button for testing
#         exitBtn = ttk.Frame(self)
#         exitBtn.pack(fill='x', padx=10, pady=10)
#         ttk.Button(
#             exitBtn,
#             text="Exit",
#             command=self.quit
#         ).pack(side="right")

#         self.bind("<Configure", self.window_resize)

#     def window_resize(self, event):
#         width = self.winfo_width()
#         height = self.winfo_height()

#         cols = 4
#         rows = (len(self.btnWidgets) + cols - 1) // cols
#         btnSize = min(
#             (width - 40) // cols,
#             (height - 80) // rows
#         )

#         for btn in self.btnWidgets:
#             btn.config(width=btnSize, height=btnSize)

#             if btn["image"]:
#                 imgName = btn['text'].lower() if btn['text'] else ""
#                 if imgName in self.icons:
#                     try:
#                         original_img = Image.open(f"./assets/{imgName}.png")
#                         new_size = btnSize - 20  # Padding
#                         resized_img = original_img.resize((new_size, new_size), Image.LANCZOS)
#                         new_photo = ImageTk.PhotoImage(resized_img)
#                         btn.config(image=new_photo)
#                         btn.image = new_photo
#                     except Exception:
#                         print("An error occured. Please debug")  # Keep reference
    
#     def click(self, name):
#         try:
#             self.command.press(name.lower())
#         except Exception:
#             messagebox.showerror(f'Failed to load {name}')

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()