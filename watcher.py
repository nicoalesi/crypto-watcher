from ctypes import windll
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import font
from tkinter import ttk


#--------------------------------- Costants ----------------------------------#

# List of all cryptos supported
CRYPTOS = [
    "Bitcoin",
    "Ethereum",
    "Ripple",
    "Solana",
    "Litecoin",
    "Dogecoin",
    "Shiba Inu",
]

# List of all cryptos' symbols
SYMBOLS = ["BTC", "ETH", "XRP", "SOL", "LTC", "DOGE", "SHIB"]


#----------------------------- Global variables ------------------------------#

# Temporary fake data for testing
data = {
    "1D": [x for x in range(100)],
    "1M": [x**2 for x in range(100)],
    "1Y": [(2.7178)**x for x in range(100)],
}

cp = {
    "1D": "10%",
    "1M": "13%",
    "1Y": "19.23%",
}


#------------------------- Graphical User Interface --------------------------#

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

# Create main title
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

# Set up window vertical scrolling
canvas.configure(yscrollcommand = scrollbar.set)
scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# Set up crypto items' fonts
# CI stands for Crypto Item
CI_name_font = font.Font(family = "Cascadia Code", size = 36)
CI_symbol_font = font.Font(family = "Cascadia Code", size = 24)
CI_price_font = font.Font(family = "Cascadia Code", size = 24)
CI_price_change_font = font.Font(family = "Cascadia Code", size = 18)
CI_button_font = font.Font(family = "Cascadia Code", size = 15)
    

# Switch view between 1 day / 1 month / 1 year data
def switch_view(view, price_change_label, plot, graph):
    # Clear plot
    plot.cla()

    # Change plot values
    plot.plot([x for x in range(100)], data[view])

    # Delete axis
    plot.axis("off")

    # Update graph
    graph.draw()

    # Update price change
    price_change_label.config(text = cp[view])


# Create crypto's row item
def create_crypto_item(title, symbol):
    # Set up crypto's row frame
    frame = tk.Frame(master = canvas)

    # Set up crypto's name label
    name_label = ttk.Label(
        master = frame,
        text = title,
        font = CI_name_font,
        width = 10,
    )

    # Create crypto's name label
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

    # Create crypto's symbol label
    symbol_label.grid(
        row = 2,
        column = 0,
        rowspan = 2,
        sticky = tk.NW,
        padx = 10,
    )

    # Set up figure
    figure = Figure(figsize = (5, 2), dpi = 100)

    # Add plot
    plot = figure.add_subplot(111)

    # Add plot values
    plot.plot(data["1D"], data["1D"])

    # Delete axis
    plot.axis("off")

    # Set up graph
    graph = FigureCanvasTkAgg(figure, master = frame)
    
    # Create graph
    graph.get_tk_widget().grid(row = 0, column = 1, rowspan = 4, padx = 10)

    # Set up crypto's price label
    price_label = ttk.Label(
        master = frame,
        text = "123,43.23",
        font = CI_price_font,
        width = 12,
        anchor = tk.SE,
    )

    # Create crypto's price label
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

    # Create crypto's price change label
    price_change_label.grid(
        row = 1,
        column = 2,
        columnspan = 3,
        sticky = tk.E, 
        padx = 10,
    )

    # Set up '1 day' button
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

    # Set up '1 month' button
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

    # Set up '1 year' button
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

    # Create all buttons
    day_button.grid(row = 2, column = 2, rowspan = 2, sticky = tk.E)
    month_button.grid(row = 2, column = 3, rowspan = 2, sticky = tk.E)
    year_button.grid(row = 2, column = 4, rowspan = 2, sticky = tk.E)

    # Return crypto's frame
    return frame


# Create all crypto items
for i, crypto in enumerate(CRYPTOS):
    symbol = SYMBOLS[i]
    canvas.create_window(580, 100 + i * 250, window = create_crypto_item(crypto, symbol))

# Create canvas
canvas.pack(expand = True, fill = "both", anchor = "ne")

# Run
window.mainloop()