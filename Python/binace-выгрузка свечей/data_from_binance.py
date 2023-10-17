apikey = '***'
secretkey = '***'

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
client = Client(apikey, secretkey)

tickers = client.get_all_tickers()
print(tickers)# выгружает в одну строчку, не так как в видео по столбцам
tickers[1]['price']
print(tickers)# не работает вывод первой монеты

ticker_df = pd.DataFrame(tickers)
print(ticker_df)#выводит всё ОК

ticker_df.tail()
print(ticker_df.tail)# не выводит первые 5 символов, повторило результат сроки 14

ticker_df.head()
print(ticker_df.head)# не выводит последние 5 символов, повторило результат строки 14


ticker_df.set_index('symbol', inplace=True)
print(ticker_df.set_index)#выводит всё ОК

float(ticker_df.loc['ETHBTC']['price'])
print(ticker_df.loc)#ничего не происходит

depth = client.get_order_book(symbol='BTCUSDT')
print(depth)# выгружает в одну строчку, не так как в видео по столбцам

historical = client.get_historical_klines('ETHBTC', Client.KLINE_INTERVAL_1DAY, '1 august 2023')
print(historical)# выгружает в одну строчку, не так как в видео по столбцам