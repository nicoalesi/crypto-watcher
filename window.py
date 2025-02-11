from ctypes import windll
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import font
from tkinter import ttk


class MyWindow:
    def __init__(self, title, width, height, isResizable = False):
        self.window = tk.Tk()
        windll.shcore.SetProcessDpiAwareness(1)
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(isResizable, isResizable)

        self.title_font = font.Font(family = "Cascadia Code", size = 20)
        self.title_label = ttk.Label(
            master = self.window,
            text = "Crypto Watcher",
            font = self.title_font,
        )
        self.title_label.pack(fill = tk.Y, pady = 10)

        self.canvas = tk.Canvas(
            master = self.window,
            scrollregion = (0, 0, 1400, 1700),
            bd = 0,
            highlightthickness = 0,
        )

        self.scrollbar = tk.Scrollbar(
            master = self.window,
            orient = "vertical",
            command = self.canvas.yview,
        )

        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

        self.crypto_items = []

        items = ["Bitcoin", "Ethereum", "Ripple", "Solana", "Litecoin", "Dogecoin", "Shiba Inu"]
        symbols = ["BTC", "ETH", "XRP", "SOL", "LTC", "DOGE", "SHIB"]
        x = 580
        y = 100

        for i, text in enumerate(items):
            self.add_crypto_item(x, y, text, symbols[i], {})

        self.window.mainloop()

    def add_crypto_item(self, x, y, name, symbol, data):
        frame = tk.Frame(master = self.canvas)

        name_font = font.Font(family = "Cascadia Code", size = 36)
        symbol_font = font.Font(family = "Cascadia Code", size = 24)
        price_font = font.Font(family = "Cascadia Code", size = 24)
        price_change_font = font.Font(family = "Cascadia Code", size = 18)
        button_font = font.Font(family = "Cascadia Code", size = 15)

        name_label = ttk.Label(master = frame, text = name, font = name_font, width = 10)
        name_label.grid(row = 0, column = 0, rowspan = 2, sticky = tk.SW, padx = 10)

        symbol_label = ttk.Label(master = frame, text = symbol, font = symbol_font, width = 10)
        symbol_label.grid(row = 2, column = 0, rowspan = 2, sticky = tk.NW, padx = 10)

        figure = Figure(figsize = (5, 2), dpi = 100)

        y = [i**2 for i in range(101)]

        plot1 = figure.add_subplot(111)
        plot1.plot(y)
        plot1.axis("off")

        graph = FigureCanvasTkAgg(figure, master = frame)
        
        graph.get_tk_widget().grid(row = 0, column = 1, rowspan = 4, padx = 10)

        price_label = ttk.Label(master = frame, text = "123,43.23", font = price_font, width = 12, anchor = tk.SE)
        price_label.grid(row = 0, column = 2, columnspan = 3, sticky = tk.SE, padx = 10)

        price_change_label = ttk.Label(master = frame, text = "2.3%", font = price_change_font, width = 10, anchor = tk.E)
        price_change_label.grid(row = 1, column = 2, columnspan = 3, sticky = tk.E, padx = 10)

        day_button = tk.Button(master = frame, text = "1D", height = 2, width = 4, bd = 0, font = button_font)
        month_button = tk.Button(master = frame, text = "1M", height = 2, width = 4, bd = 0, font = button_font)
        year_button = tk.Button(master = frame, text = "1Y", height = 2, width = 4, bd = 0, font = button_font)

        day_button.grid(row = 2, column = 2, rowspan = 2, sticky = tk.E)
        month_button.grid(row = 2, column = 3, rowspan = 2, sticky = tk.E)
        year_button.grid(row = 2, column = 4, rowspan = 2, sticky = tk.E)

        self.canvas.create_window(x, y, window = frame)


if __name__ == "__main__":
    window = MyWindow("Watcher", 1200, 740)
    