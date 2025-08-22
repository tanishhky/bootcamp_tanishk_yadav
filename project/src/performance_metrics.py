import numpy as np
import yfinance as yf

def compare_with_index(stock="BRK-B", index="^GSPC", start="2018-01-01"):
    data = yf.download([stock, index], start=start)["Adj Close"].dropna()
    returns = data.pct_change().dropna()
    cumulative = (1+returns).cumprod()

    outperformance = cumulative[stock].iloc[-1] > cumulative[index].iloc[-1]
    return cumulative, outperformance

def volatility(stock="BRK-B", start="2018-01-01"):
    data = yf.download(stock, start=start)["Adj Close"]
    return data.pct_change().std()
