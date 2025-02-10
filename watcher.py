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
title_label.pack(fill = tk.Y, pady = 10)

# Set up canvas
canvas = tk.Canvas(master = window, scrollregion = (0, 0, 1400, 1600))

# Set up scrollbar
scrollbar = tk.Scrollbar(master = window, orient = "vertical", command = canvas.yview)
canvas.configure(yscrollcommand = scrollbar.set)
scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# Set up mousewheel scrolling
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 120), "units"))

canvas.pack(expand = True, fill = "both", anchor = "ne")

# Run
window.mainloop()