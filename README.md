# Crypto watcher

**Crypto watcher is a program to visualize the historical data of 7 selected cryptocurrencies.**

It is designed to be minimal and easy to use. It displays cryptos' *name, symbol, latest price* and *price change* during the selected time span.

## Index
 - [Supported cryptocurrencies](#supported-cryptocurrencies)
 - [Usage](#usage)
 - [GUI](#gui)
 - [API](#api)

----

## Supported cryptocurrencies

Only 7 cryptocurrencies are supported because of API's limits but the code is written in such a way that scaling the number of cryptos is easy and straightforward.

Provided that those cryptos are supported by the API, they can just be added to `CRYPTOS` and `SYMBOLS` lists to be displayed along with their graphs and their data.

At the moment of release these are already supported:

 - Bitcoin
 - Ethereum
 - Ripple
 - Solana
 - Litecoin
 - Dogecoin
 - Shiba Inu

## Usage

To use this program follow these steps:

1. Download all the files from GitHub.
2. Open the terminal.
3. Move to the directory where the project is located.
4. Make sure to have python installed on your computer.
5. Check that all the modules listed in ***requirements.txt*** are present on your computer. <br>
   If one of them is missing you can install it running the following command:

   `pip install <module>`
   
7. Run the main file ***watcher.py*** using the following command:
   
   `python watcher.py`

## GUI

Everything is contained in a fixed-size window. There is a scrollable canvas with all the cryptocurrencies organized in rows.

The price change label shows an arrow indicating the crypto's trend. It also affects the color of graph, latest price and price change, which can be green or red.

<br>

![](/preview.png)

## API

To make this program **Alpha Vantage**'s API has been used. It's free up to 25 requests per day. <br>
Check its [documentation](https://www.alphavantage.co/documentation/) for further information.
