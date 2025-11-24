import pandas as pd

def ema_strategy(data):
    data['EMA20'] = data['close'].ewm(span=20, adjust=False).mean()
    data['EMA50'] = data['close'].ewm(span=50, adjust=False).mean()

    last = data.iloc[-1]

    if last['EMA20'] > last['EMA50']:
        return "BUY"
    elif last['EMA20'] < last['EMA50']:
        return "SELL"
    else:
        return "HOLD"
