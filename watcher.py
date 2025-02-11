from ctypes import windll
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import font
from tkinter import ttk

# Set up window
window = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1)
window.title("Crypto watcher")
window.geometry("1200x740")
window.resizable(False, False)

# Set up main font
title_font = font.Font(family = "Cascadia Code", size = 20)

# Set up main title
title_label = ttk.Label(master = window, text = "Crypto watcher", font = title_font)
title_label.pack(fill = tk.Y, pady = 10)

# Set up canvas
canvas = tk.Canvas(master = window, scrollregion = (0, 0, 1400, 1700), bd = 0, highlightthickness = 0)

# Set up scrollbar
scrollbar = tk.Scrollbar(master = window, orient = "vertical", command = canvas.yview)
canvas.configure(yscrollcommand = scrollbar.set)
scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# Set up mousewheel scrolling
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 120), "units"))

# Set up row fonts
row_name_font = font.Font(family = "Cascadia Code", size = 36)
row_symbol_font = font.Font(family = "Cascadia Code", size = 24)
row_price_font = font.Font(family = "Cascadia Code", size = 24)
row_price_change_font = font.Font(family = "Cascadia Code", size = 18)
row_button_font = font.Font(family = "Cascadia Code", size = 15)

# Create graph
def create_graph(master):
    figure = Figure(figsize = (5, 2), dpi = 100)

    y = [i**2 for i in range(101)]

    plot1 = figure.add_subplot(111)
    plot1.plot(y)
    plot1.axis("off")

    graph = FigureCanvasTkAgg(figure, master = master)

    return graph
    

# Create crypto's row
def create_row(title, symbol, data):
    # Set up row's frame
    row_frame = tk.Frame(master = canvas)

    # Set up crypto's name label
    name_label = ttk.Label(master = row_frame, text = title, font = row_name_font, width = 10)
    name_label.grid(row = 0, column = 0, rowspan = 2, sticky = tk.SW, padx = 10)

    # Set up crypto's symbol label
    symbol_label = ttk.Label(master = row_frame, text = symbol, font = row_symbol_font, width = 10)
    symbol_label.grid(row = 2, column = 0, rowspan = 2, sticky = tk.NW, padx = 10)

    # Set up canvas for graph
    # row_canvas = tk.Canvas(master = row_frame, height = 120, width = 500)
    # row_canvas.configure(bg="red")
    
    row_canvas = create_graph(row_frame)
    
    row_canvas.get_tk_widget().grid(row = 0, column = 1, rowspan = 4, padx = 10)

    # Set up crypto's price label
    price_label = ttk.Label(master = row_frame, text = "123,43.23", font = row_price_font, width = 12, anchor = tk.SE)
    price_label.grid(row = 0, column = 2, columnspan = 3, sticky = tk.SE, padx = 10)

    # Set up crypto's price change label
    price_change_label = ttk.Label(master = row_frame, text = "2.3%", font = row_price_change_font, width = 10, anchor = tk.E)
    price_change_label.grid(row = 1, column = 2, columnspan = 3, sticky = tk.E, padx = 10)

    # Set up time buttons
    day_button = tk.Button(master = row_frame, text = "1D", height = 2, width = 4, bd = 0, font = row_button_font)
    month_button = tk.Button(master = row_frame, text = "1M", height = 2, width = 4, bd = 0, font = row_button_font)
    year_button = tk.Button(master = row_frame, text = "1Y", height = 2, width = 4, bd = 0, font = row_button_font)

    day_button.grid(row = 2, column = 2, rowspan = 2, sticky = tk.E)
    month_button.grid(row = 2, column = 3, rowspan = 2, sticky = tk.E)
    year_button.grid(row = 2, column = 4, rowspan = 2, sticky = tk.E)

    # Return crypto's frame
    return row_frame

items = ["Bitcoin", "Ethereum", "Ripple", "Solana", "Litecoin", "Dogecoin", "Shiba Inu"]
symbols = ["BTC", "ETH", "XRP", "SOL", "LTC", "DOGE", "SHIB"]

for i, text in enumerate(items):
    canvas.create_window(580, 100 + i * 250, window = create_row(text, symbols[i], {}))

# Pack canvas
canvas.pack(expand = True, fill = "both", anchor = "ne")

# Run
window.mainloop()