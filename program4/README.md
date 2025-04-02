# Stock Portfolio Tracker

This is a Python program. It allows users to manage and analyze their stock investments by retrieving real-time stock prices and calculating gains or losses. The application uses a graphical user interface (GUI) built with `wxPython` and integrates with the **Finnhub API** for stock data.

## Features
- **Database Integration**: Retrieves stock data (company name, symbol, purchase price, and shares) from an SQLite database (`tech_stocks.db`).
- **Real-Time Stock Prices**: Fetches current stock prices using the Finnhub API.
- **Gain/Loss Calculation**: Calculates the net gain or loss for each stock and the total portfolio.
- **User-Friendly GUI**: Displays stock information in a table format with columns for company name, symbol, purchase price, current price, shares, and gain/loss.
- **Dynamic Updates**: Shows the current date and time, and updates the portfolio data on demand.

## Dependencies
- Python 3.x
- `wxPython` library
- `requests` library
- `python-dotenv` library
- SQLite database (`tech_stocks.db`)
- Finnhub API key (stored in a `.env` file):
    You need to create the .env file and store the Finnhub API key. Follow these steps:
    1. Create a file named `.env` in the same directory of `stocks.py`.
    2. Inside the .env file, add the following line: `FINNHUB_API_KEY=your_api_key_here`
    3. Replace `your_api_key_here` with your actual Finnhub API key.
        - Go to https://finnhub.io/ and click `Get free API key` button.

