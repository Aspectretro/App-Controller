import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from control import ctrl

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.command = ctrl()
        
        # Load icons FIRST with default size
        self.icons = {}
        self.app_names = ["Word", "Chrome", "File", "Music", 
                         "Settings", "Lightroom", "Logseq"]
        self.load(80)  # Initial load before UI
        
        # Window configuration
        self.title("App Controller")
        self.geometry("600x600")
        self.minsize(400, 400)
        
        # Main container
        self.main_frame = tk.Frame(self, bg='#f0f0f0')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Initial UI setup
        self.setup_ui()
        
        # Exit button
        exit_frame = tk.Frame(self)
        exit_frame.pack(fill='x', padx=20, pady=(0, 20))
        ttk.Button(exit_frame, text="Exit", command=self.quit).pack(side='right')
        
        self.bind("<Configure>", self.on_window_resize)
        self.after(100, self.force_layout_pass)

    # load on startup
    def load(self, size):
        """Load/resize icons to specified size"""
        for name in self.app_names:
            try:
                img = Image.open(f"./assets/{name}.png")
                img = img.resize((size-20, size-20), Image.LANCZOS)
                self.icons[name.lower()] = ImageTk.PhotoImage(img)
            except Exception:
                print(f"Failed to load {name} icon")
                self.icons[name.lower()] = None

    def force_layout_pass(self):
        """Force Tkinter to calculate actual window dimensions"""
        self.update_idletasks()  # Complete all pending operations
        self.setup_ui()  # Build UI with actual dimensions
    
    def setup_ui(self):
        """Initialize or rebuild the UI elements"""
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.buttons = []
        
        # Calculate layout parameters
        cols_per_row = 4  # Number of buttons per row
        available_width = self.main_frame.winfo_width() - 40  # Account for padding
        available_height = self.main_frame.winfo_height() - 40
        
        if available_width <= 0 or available_height <= 0:
            return
            
        # Calculate button size based on available space
        button_size = min(
            available_width // cols_per_row,
            available_height // ((len(self.app_names) + cols_per_row - 1) // cols_per_row)
        )
        button_size = max(80, min(button_size, 150))  # Limit between 80 and 150px

        self.load(button_size)
        
        # Load/resize images
        for name in self.app_names:
            try:
                img = Image.open(f"./assets/{name}.png")
                img = img.resize((button_size-20, button_size-20), Image.LANCZOS)
                self.icons[name.lower()] = ImageTk.PhotoImage(img)
            except Exception:
                print(f"Failed to load {name} icon")
                self.icons[name.lower()] = None
        
        # Create buttons in grid
        for index, name in enumerate(self.app_names):
            row = index // cols_per_row
            col = index % cols_per_row
            
            btn = tk.Button(
                self.main_frame,
                image=self.icons.get(name.lower()),
                text=name if not self.icons.get(name.lower()) else "",
                compound=tk.TOP,
                command=lambda n=name.lower(): self.click(n),
                borderwidth=2,
                relief="raised",
                bg='white',
                activebackground='#e0e0e0'
            )
            
            # Make button square
            btn.config(width=button_size, height=button_size)
            btn.grid(
                row=row,
                column=col,
                padx=5,
                pady=5,
                sticky="nsew"
            )
            self.buttons.append(btn)
        
        # Configure grid weights
        for r in range((len(self.app_names) + cols_per_row - 1) // cols_per_row):
            self.main_frame.grid_rowconfigure(r, weight=1, uniform="row")
        for c in range(cols_per_row):
            self.main_frame.grid_columnconfigure(c, weight=1, uniform="col")
    
    def on_window_resize(self, event):
        """Handle window resize events"""
        if event.widget == self and self.winfo_width() > 50:  # Only respond to main window resize
            self.setup_ui()
    
    def click(self, name):
        try:
            self.command.press(name)
        except Exception:
            messagebox.showerror("Error", f'Failed to load {name}')

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