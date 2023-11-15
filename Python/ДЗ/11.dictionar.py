data = {
    'symbol': 'BTCUSDT',
    'price': 34187.4,
    'volume': 47731000
}
data['stock_exchange'] = 'BINANCE'

print(data['symbol'], data['stock_exchange'])

data = {
    'symbol': 'BNBUSDT',
    'price': 225.71,
    'volume': 188538000,
}
data['stock_exchange'] = 'BYBIT'

print(data['symbol'], data['stock_exchange'])

data = {
    'symbol': 'TRXUSDT',
    'price': 0.09458,
    'volume': 133836000
}
data['stock_exchange'] = 'FTX'

print(data['symbol'], data['stock_exchange'])



#Добавить в каждый словарь новую пару с названием биржи, 
# на которой торгуется актив. Распечатать на экране названия 
# каждой монеты и биржи, на которой она торгуется.  