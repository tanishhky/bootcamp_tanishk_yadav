import numpy as np
import pandas as pd
import yfinance as yf

def calculate_beta(stock, market="^GSPC", start="2018-01-01", end="2025-01-01"):
    data = yf.download([stock, market], start=start, end=end)["Adj Close"].dropna()
    returns = data.pct_change().dropna()
    cov = np.cov(returns[stock], returns[market])[0,1]
    var = np.var(returns[market])
    return cov / var

def portfolio_betas(holdings):
    betas = {}
    total_value = 0

    for _, row in holdings.iterrows():
        beta = calculate_beta(row["Ticker"])
        price = yf.Ticker(row["Ticker"]).history(period="1d")["Close"].iloc[-1]
        value = price * row["Number of shares"]
        betas[row["Ticker"]] = {"beta": beta, "value": value}
        total_value += value

    # simple vs weighted
    simple_avg = np.mean([b["beta"] for b in betas.values()])
    weighted_avg = sum([b["beta"]*b["value"] for b in betas.values()]) / total_value
    return betas, simple_avg, weighted_avg
