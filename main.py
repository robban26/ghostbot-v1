from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
import time

from config import API_KEY, API_SECRET, BASE_URL
from strategies.basic_strategy import run_strategy

client = TradingClient(API_KEY, API_SECRET, paper=True)
data_client = StockHistoricalDataClient(API_KEY, API_SECRET)

symbols = ["AAPL", "TSLA", "MSFT"]

def get_bars(symbol):
    request_params = StockBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=TimeFrame.Minute,
        limit=3
    )
    bars = data_client.get_stock_bars(request_params)
    return bars.data[symbol]

def trade_loop():
    while True:
        for symbol in symbols:
            bars = get_bars(symbol)
            decision = run_strategy(bars)

            print(f"{symbol}: {decision}")

            if decision == "buy":
                client.submit_order(
                    symbol=symbol,
                    qty=1,
                    side="buy",
                    type="market",
                    time_in_force="day",
                )
            elif decision == "sell":
                client.submit_order(
                    symbol=symbol,
                    qty=1,
                    side="sell",
                    type="market",
                    time_in_force="day",
                )

        time.sleep(60)

if __name__ == "__main__":
    trade_loop()
