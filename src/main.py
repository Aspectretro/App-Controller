import tkinter as tk
from tkinter import ttk, Menu
from PIL import Image, ImageTk
from control import ctrl  # Assuming this contains your application control logic
from systemTray import TrayManage
from startup import Startup

class App(tk.Tk):
    def __init__(self): # TODO: window icon
        super().__init__()
        self.command = ctrl()
        
        # Fixed button and window configuration
        self.button_size = 100  # pixels 
        self.padding = 1 # window padding
        self.buttons_per_row = 4
        self.configure(bg="#f5f5f5") # Lightgray window background
        
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
        self.create_menu()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Startup Manager
        self.startup = Startup("App Controller")
        self.create_startup_menu()
        
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

# Menu config    
    def create_menu(self):
        menubar = tk.Menu(self)  # Main menu bar
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit_app)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Options menu (renamed from "Option" to be consistent)
        options_menu = tk.Menu(menubar, tearoff=0)
        
        # Tray option
        self.tray_var = tk.BooleanVar(value=False)
        options_menu.add_checkbutton(
            label="Minimize to tray when closed",
            variable=self.tray_var,
            command=self.toggle_tray
        )
        
        # Startup option will be added later in create_startup_menu
        menubar.add_cascade(label="Options", menu=options_menu)
        
        self.config(menu=menubar)
        menubar.configure(bg="#e0e0e0")
        return menubar

# System Tray
    def toggle_tray(self):
        self.trayManage.set_tray(self.tray_var.get())
    
    def on_close(self):
        if self.tray_var.get():
            self.trayManage.min_to_tray()
        else:
            self.destroy()

# Windows Startup
    def create_startup_menu(self):
        """Add startup option"""
        menubar = self.nametowidget(self["menu"])
        options = menubar.nametowidget(menubar.entrycget("Options", "menu"))

        self.startup_Var = tk.BooleanVar(value=self.startup.is_enabled())
        options.add_checkbutton(
            label="Open on startup",
            variable=self.startup_Var,
            command=self.toggle_startup
        )
    
    def toggle_startup(self):
        if self.startup_Var.get():
            self.startup.enable_start()
        else:
            self.startup.disable_start()

# Default UI configs (buttons, icons)
    def quit_app(self):
        self.trayManage.quit_app()

    def load_icons(self):
        """Load all icons at fixed size"""
        self.icons = {}
        app_names = ["Word", "Chrome", "File", "Spotify", 
                    "Settings", "Lightroom", "Logseq",
                    "Discord", "zoom", "Microsoft Edge",
                    "Calculator", "Powerpoint"]
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
            ("spotify", "Spotify"),
            ("file", "File"),
            ("settings", "Settings"),
            ("lightroom", "Lightroom"),
            ("logseq", "Logseq"),
            ('discord', "Discord"),
            ("zoom", "zoom"),
            ("microsoft edge", "Microsoft Edge"),
            ("calculator", "Calculator"),
            ("powerpoint", "Powerpoint")
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