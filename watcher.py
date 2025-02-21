from ctypes import windll
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import tkinter as tk
from tkinter import font


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

# API key
API_KEY = "XXXXXXXXXXXXXXX"


#------------------------------------ API ------------------------------------#

# Dictionary of dictionaries in which historical data are stored
data = {
    "3M": {},
    "2Y": {},
}

for symbol in SYMBOLS:
    # for placeholder, frequency, quantity in data_information:
        # Delete 2nd for loop and populate the dictionary manually
        # url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_{frequency.upper()}&symbol={symbol}&market=EUR&apikey={API_KEY}"
        # response = requests.get(url).json()
        # days = list(response[f"Time Series (Digital Currency {frequency})"].values())
        # data[placeholder][symbol] = [ float(day["4. close"]) for day in days[:100] ]
    with open("daily_btc.txt") as file:
        content = file.read()
        prices = content.split(",")
        floats = [ float(price) for price in prices ]

    data["3M"][symbol] = floats[::-1]

    with open("weekly_btc.txt") as file:
        content = file.read()
        prices = content.split(",")
        floats = [ float(price) for price in prices[:90] ]
    
    data["2Y"][symbol] = floats[::-1]


#----------------------------- Global variables ------------------------------#

# Dictionary to store latest prices
prices = { symbol:data["3M"][symbol][-1] for symbol in SYMBOLS }

# Dictionary of dictionaries to store price changes over a fixed amount of time
price_change = {
    "3M": {},
    "2Y": {},
}

# Populate "price_change" dictionary
for symbol in SYMBOLS:
    # "3 months" price changes
    start_price = data["3M"][symbol][0]
    end_price = data["3M"][symbol][-1]
    price_change["3M"][symbol] = (end_price / start_price - 1) * 100

    # "2 years" price changes
    start_price = data["2Y"][symbol][0]
    end_price = data["2Y"][symbol][-1]
    price_change["2Y"][symbol] = (end_price / start_price - 1) * 100


#------------------------- Graphical User Interface --------------------------#

# Set up window
window = tk.Tk()
windll.shcore.SetProcessDpiAwareness(1)
window.title("Crypto watcher")
window.geometry("1200x740")
window.resizable(False, False)
window.config(bg = "white")

# Set up title font
title_font = font.Font(family = "Cascadia Code", size = 20)

# Set up main title
title_label = tk.Label(
    master = window,
    text = "Crypto watcher",
    font = title_font,
    bg = "white",
)

# Create main title
title_label.pack(fill = tk.Y, pady = 10)

# Set up canvas
canvas = tk.Canvas(
    master = window,
    scrollregion = (0, 0, 1400, 1700),
    bd = 0,
    bg = "white",
    highlightthickness = 0,
)

# Set up scrollbar
scrollbar = tk.Scrollbar(
    master = window,
    orient = "vertical",
    command = canvas.yview,
)

# Set up window vertical scrolling
canvas.config(yscrollcommand = scrollbar.set)
scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# Set up crypto items' fonts
# CI stands for Crypto Item
CI_name_font = font.Font(family = "Cascadia Code", size = 36)
CI_symbol_font = font.Font(family = "Cascadia Code", size = 24)
CI_price_font = font.Font(family = "Cascadia Code", size = 24)
CI_price_change_font = font.Font(family = "Cascadia Code", size = 18)
CI_button_font = font.Font(family = "Cascadia Code", size = 15)
    

# Switch view between 1 day / 1 month / 1 year data
def switch_view(view, symbol, price_label, price_change_label, plot, graph):
    # Set up trend symbol and trend color
    trend, trend_color = ("▼", "#D32F2F") if price_change["3M"][symbol] < 0 \
                                          else ("▲", "#388E3C")

    # Clear plot
    plot.cla()

    # Change plot values
    plot.plot(
        [ x for x in range(len(data[view][symbol])) ],
        data[view][symbol],
        color = trend_color,
    )

    # Delete axis
    plot.axis("off")

    # Update graph
    graph.draw()

    # Update price change
    price_change_label.config(
        text = f"{trend} {abs(price_change[view][symbol]):.2f}%",
    )

    price_label.config(fg = trend_color)


# Create crypto's row item
def create_crypto_item(title, symbol):
    # Set up crypto's row frame
    frame = tk.Frame(master = canvas, bg = "white")

    # Set up trend symbol and trend color
    trend, trend_color = ("▼", "#D32F2F") if price_change["3M"][symbol] < 0 \
                                          else ("▲", "#388E3C")

    # Set up crypto's name label
    name_label = tk.Label(
        master = frame,
        text = title,
        font = CI_name_font,
        width = 10,
        bg = "white",
        anchor = tk.W,
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
    symbol_label = tk.Label(
        master = frame,
        text = symbol,
        font = CI_symbol_font,
        width = 10,
        bg = "white",
        anchor = tk.W,
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
    figure = Figure(figsize = (5, 1.5), dpi = 100)

    # Add plot
    plot = figure.add_subplot(111)

    # Add plot values
    plot.plot(
        [ x for x in range(len(data["3M"][symbol])) ],
        data["3M"][symbol],
        color = trend_color,
    )

    # Delete axis
    plot.axis("off")

    # Set up graph
    graph = FigureCanvasTkAgg(figure, master = frame)
    
    # Create graph
    graph.get_tk_widget().grid(row = 0, column = 1, rowspan = 4, padx = 10)

    # Set up price label's text
    if prices[symbol] > 100000:
        price_text = f"{(prices[symbol] / 1000):.2f}K"
    elif prices[symbol] < 0.0001:
        price_text = "< 0.0001"
    else:
        price_text = prices[symbol]

    # Set up crypto's price label
    price_label = tk.Label(
        master = frame,
        text = f"{price_text} EUR",
        font = CI_price_font,
        width = 12,
        anchor = tk.SE,
        fg = trend_color,
        bg = "white",
    )

    # Create crypto's price label
    price_label.grid(
        row = 0,
        column = 2,
        columnspan = 2,
        sticky = tk.SE,
        padx = 10,
    )

    # Set up crypto's price change label
    price_change_label = tk.Label(
        master = frame,
        text = f"{trend} {abs(price_change["3M"][symbol]):.2f}%",
        font = CI_price_change_font,
        width = 10,
        anchor = tk.E,
        fg = trend_color,
        bg = "white",
    )

    # Create crypto's price change label
    price_change_label.grid(
        row = 1,
        column = 2,
        columnspan = 2,
        sticky = tk.E, 
        padx = 10,
    )

    # Set up '3 months' button
    months_button = tk.Button(
        master = frame,
        text = "3M",
        height = 2,
        width = 4,
        bd = 0,
        font = CI_button_font,
        command = lambda: switch_view(
            "3M",
            symbol,
            price_label,
            price_change_label,
            plot,
            graph,
        ),
        bg = "white",
    )

    # Set up '2 years' button
    years_button = tk.Button(
        master = frame,
        text = "2Y",
        height = 2, 
        width = 4,
        bd = 0,
        font = CI_button_font,
        command = lambda: switch_view(
            "2Y",
            symbol,
            price_label,
            price_change_label,
            plot,
            graph,
        ),
        bg = "white",
    )


    # Create all buttons
    months_button.grid(
        row = 2,
        column = 2,
        rowspan = 2,
        sticky = tk.E,
    )

    years_button.grid(
        row = 2,
        column = 3,
        rowspan = 2,
        sticky = tk.E,
        padx = 35,
    )

    # Return crypto's frame
    return frame


# Create all crypto items
for i, crypto in enumerate(CRYPTOS):
    symbol = SYMBOLS[i]
    canvas.create_window(
        580,
        100 + i * 250,
        window = create_crypto_item(crypto, symbol),
    )

# Create canvas
canvas.pack(expand = True, fill = "both", anchor = "ne")

# Run
window.mainloop()