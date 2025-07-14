import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Tkinter Window Demo')
window.geometry('600x400+50+50')
# TODO: add icon


def re_press(event):
    print(event)

btn = ttk.Button(window, text="Save")
btn.bind('<RETURN>', re_press)

window.mainloop()