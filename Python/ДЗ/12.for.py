# создать список из 10 активов. С помощью цикла  for и f’строки распечатать: “Рыночный ордер на (название актива) открыт.

symbol = ['ETHUSDT', 'BNXUSDT', 'XRPUSDT', 'FLOWUSDT', 'ROSEUSDT', 'FLOKIUSDT', 'STORJUSDT', 'BNBUSDT', 'CFXUSDT', 'RUNEUSDT']

for symbols in symbol:
    print(f'Рыночный ордер на {symbols} открыт.')
