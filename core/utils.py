import pandas as pd


def SMA(array, n):
    """Simple Moving Average (SMA): Smooths price data by averaging closing prices over a period."""
    return pd.Series(array).rolling(n).mean()


def RSI(array, n):
    """Relative Strength Index (RSI): Measures the speed and change of price movements to identify overbought or oversold conditions."""
    gain = pd.Series(array).diff()
    loss = gain.copy()
    gain[gain < 0] = 0
    loss[loss > 0] = 0
    rs = gain.ewm(n).mean() / loss.abs().ewm(n).mean()
    return 100 - 100 / (1 + rs)
