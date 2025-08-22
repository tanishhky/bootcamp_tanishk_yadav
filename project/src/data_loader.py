import pandas as pd
import yfinance as yf

def load_holdings(filepath="../data/raw/holdings.csv"):
    return pd.read_csv(filepath)

def fetch_prices(tickers, start="2018-01-01", end="2025-01-01"):
    data = yf.download(tickers, start=start, end=end)["Adj Close"]
    return data
