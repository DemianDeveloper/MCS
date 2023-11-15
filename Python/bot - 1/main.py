from binance.client import Client
import keys
import pandas as pd
import time

Client = Client(keys.api_key, keys.api_secret, testnet=True)

def top_coin():
    all_tickers = pd.DataFrame(Client.get_ticker()) # читать с конца предолжения, обращается к библиотеке бинансе 
    usdt = all_tickers[all_tickers.symbol.str.contains('usdt')] # из всего массива верхней строчки нам нужны пары только к USDT 
    work = usdt[~((usdt.symbol.str.contains('UP')) | (usdt.symbol.str.contains('down')))] # отсеиваем те, что не торгуются в течение дня 
    top_coin = work[work.priceChangePercent == work.priceChangePercent.max()] # сортируем монеты по активности начиная с мах. В начале списка будут те, что торгуюся больше всего 
    top_coin = top_coin.symbol.values[0] # обращаемся к прошлой строке, покажи нам значение символосо с нулём 
    return top_coin

print(top_coin()) # запускаем функцию к нашему эккаунту    

def last_data(sybmol, interval, lookback): # проверяем растёт ли сейчас
    