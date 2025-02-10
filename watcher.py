from ctypes import windll
import tkinter as tk
from tkinter import font
from tkinter import ttk

# Set up window
window = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1)
window.title("Crypto watcher")
window.geometry("1400x800")

# Set up main font
font = font.Font(family = "Cascadia Code", size = 20)

# Set up main title
title_label = ttk.Label(master = window, text = "Crypto watcher", font = font)
title_label.pack()

# Run
window.mainloop()