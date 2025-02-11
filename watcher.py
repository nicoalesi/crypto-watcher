from ctypes import windll
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import font
from tkinter import ttk

cryptos = [
    "Bitcoin",
    "Ethereum",
    "Ripple",
    "Solana",
    "Litecoin",
    "Dogecoin",
    "Shiba Inu",
]

symbols = ["BTC", "ETH", "XRP", "SOL", "LTC", "DOGE", "SHIB"]

dati = {
    "1D": [x for x in range(100)],
    "1M": [x**2 for x in range(100)],
    "1Y": [(2.7178)**x for x in range(100)],
}

cp = {
    "1D": "10%",
    "1M": "13%",
    "1Y": "19.23%",
}

# Set up window
window = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1)
window.title("Crypto watcher")
window.geometry("1200x740")
window.resizable(False, False)

# Set up title font
title_font = font.Font(family = "Cascadia Code", size = 20)

# Set up main title
title_label = ttk.Label(
    master = window,
    text = "Crypto watcher",
    font = title_font,
)

title_label.pack(fill = tk.Y, pady = 10)

# Set up canvas
canvas = tk.Canvas(
    master = window,
    scrollregion = (0, 0, 1400, 1700),
    bd = 0,
    highlightthickness = 0,
)

# Set up scrollbar
scrollbar = tk.Scrollbar(
    master = window,
    orient = "vertical",
    command = canvas.yview,
)

canvas.configure(yscrollcommand = scrollbar.set)
scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# Set up mousewheel scrolling
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 120), "units"))

# Set up crypto items' fonts
# CI stands for Crypto Item
CI_name_font = font.Font(family = "Cascadia Code", size = 36)
CI_symbol_font = font.Font(family = "Cascadia Code", size = 24)
CI_price_font = font.Font(family = "Cascadia Code", size = 24)
CI_price_change_font = font.Font(family = "Cascadia Code", size = 18)
CI_button_font = font.Font(family = "Cascadia Code", size = 15)
    
def switch_view(view, price_change_label, plot, graph):
    plot.cla()
    plot.plot([x for x in range(100)], dati[view])
    plot.axis("off")
    graph.draw()

    price_change_label.config(text = cp[view])

# Create crypto's row item
def create_crypto_item(title, symbol):
    # Set up row's frame
    frame = tk.Frame(master = canvas)

    # Set up crypto's name label
    name_label = ttk.Label(
        master = frame,
        text = title,
        font = CI_name_font,
        width = 10,
    )

    name_label.grid(
        row = 0,
        column = 0,
        rowspan = 2,
        sticky = tk.SW,
        padx = 10,
    )

    # Set up crypto's symbol label
    symbol_label = ttk.Label(
        master = frame,
        text = symbol,
        font = CI_symbol_font,
        width = 10,
    )

    symbol_label.grid(
        row = 2,
        column = 0,
        rowspan = 2,
        sticky = tk.NW,
        padx = 10,
    )

    # Set up graph
    figure = Figure(figsize = (5, 2), dpi = 100)

    plot = figure.add_subplot(111)
    plot.plot(dati["1D"], dati["1D"])
    plot.axis("off")

    graph = FigureCanvasTkAgg(figure, master = frame)
    
    graph.get_tk_widget().grid(row = 0, column = 1, rowspan = 4, padx = 10)

    # Set up crypto's price label
    price_label = ttk.Label(
        master = frame,
        text = "123,43.23",
        font = CI_price_font,
        width = 12,
        anchor = tk.SE,
    )

    price_label.grid(
        row = 0,
        column = 2,
        columnspan = 3,
        sticky = tk.SE,
        padx = 10,
    )

    # Set up crypto's price change label
    price_change_label = ttk.Label(
        master = frame,
        text = "2.3%",
        font = CI_price_change_font,
        width = 10,
        anchor = tk.E,
    )

    price_change_label.grid(
        row = 1,
        column = 2,
        columnspan = 3,
        sticky = tk.E, 
        padx = 10,
    )

    # Set up time buttons
    day_button = tk.Button(
        master = frame,
        text = "1D",
        height = 2,
        width = 4,
        bd = 0,
        font = CI_button_font,
        command = lambda: switch_view(
            "1D",
            price_change_label,
            plot,
            graph,
        ),
    )

    month_button = tk.Button(
        master = frame,
        text = "1M",
        height = 2, 
        width = 4,
        bd = 0,
        font = CI_button_font,
        command = lambda: switch_view(
            "1M",
            price_change_label,
            plot,
            graph,
        ),
    )

    year_button = tk.Button(
        master = frame,
        text = "1Y",
        height = 2,
        width = 4,
        bd = 0,
        font = CI_button_font,
        command = lambda: switch_view(
            "1Y",
            price_change_label,
            plot,
            graph,
        ),
    )

    day_button.grid(row = 2, column = 2, rowspan = 2, sticky = tk.E)
    month_button.grid(row = 2, column = 3, rowspan = 2, sticky = tk.E)
    year_button.grid(row = 2, column = 4, rowspan = 2, sticky = tk.E)

    # Return crypto's frame
    return frame


for i, crypto in enumerate(cryptos):
    canvas.create_window(580, 100 + i * 250, window = create_crypto_item(crypto, symbols[i]))

# Pack canvas
canvas.pack(expand = True, fill = "both", anchor = "ne")

# Run
window.mainloop()