def run_strategy(data):
    prices = [c['close'] for c in data]
    if prices[-1] > prices[-2]:
        return "buy"
    elif prices[-1] < prices[-2]:
        return "sell"
    return "hold"
