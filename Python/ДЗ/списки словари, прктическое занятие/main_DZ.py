import requests
import pprint

symbol = "BTCUSDT" 

tickers = requests.get(f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m")
result = tickers.json()

candles_list = []

for candle in result:
    startTime = candle[0] # индекс 0 соответствует значению Kline Open Time
    openPrice = candle[1]  # индекс 1 соответствует значению Kline Open Price
    endTime = candle[6]
    closePrice = candle[4]  # индекс 4 соответствует значению Kline Close Price
    
    candles_list.append((startTime, openPrice, endTime, closePrice))

print(f"Монета: {symbol}")
print("Время открытия свечи, Цена открытия свечи, Время закрытия свечи, Цена закрытия свечи:")
pprint.pprint(candles_list)