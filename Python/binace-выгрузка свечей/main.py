apikey = 'IrfDFRnaL6LO4QdcYdC1o0KXL2FCopBNy9sBkSForYd2Q1BaNfd5LCWag4azFOxZ'
secretkey = 'U9PdyJeXxtjWfSGvg4A7DcYgQfFPpfqE0AKfwT0X4ZWHZOBLL1lmPCCn5OTkpxSg'

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
client = Client(apikey, secretkey)

tickers = client.get_all_tickers()
print(tickers)# выгружает какой-то не структурированной простынёй, не так как в видео по столбцам
tickers[1]['price']
print(tickers)# не работает вывод первой монеты

ticker_df = pd.DataFrame(tickers)
print(ticker_df)#выводит всё ОК

ticker_df.tail()
print(ticker_df.tail)# не выводит первые 5 символов, повторило результат сроки 14

ticker_df.head()
print(ticker_df.head)# не выводит последние 5 символов, повторило результат строки 14

depth = client.get_order_book(symbol='BTCUSDT')
print(depth)# выгружает какой-то не структурированной простынёй, не так как в видео по столбцам

ticker_df.set_index('symbol', inplace=True)
print(ticker_df.set_index)#выводит всё ОК

float(ticker_df.loc['ETHBTC']['price'])
print(ticker_df.loc)#ничего не происходит

historical = client.get_historical_klines('ETHBTC', Client.KLINE_INTERVAL_1DAY, '1 august 2023')
print(historical)