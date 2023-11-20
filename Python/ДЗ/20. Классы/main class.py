# active = 'SBER' #объекты 
# price = 100
# volume = 23000

# def buy():
#     return 'buy'

class Active:
    symbol = '' #переменные внутри класса = свойства
    price = None
    volume = None

    def buy(self): #создаём функцию(=метод) внутри класса, self - в себя
        return f"{self.symbol} buy"
    
Bitcoin = Active() #создали новый экземпляр класса, он наследует класс
Bitcoin.symbol = 'BTCUSDT'
Bitcoin.price = 20000

Solana = Active()
Solana.symbol = 'SOLUSDT'

print(Solana.buy())    
# print(Bitcoin.price)

class Exchanges:
    binance = None
    bybit = None
    OKX = None 

    def buy(self):  
        return f"{self.binance} buy"

    def sell(self):  
        return f"{self.binance} sell" 


all_reports = Exchanges()
all_reports.binance = 'PNL'
all_reports.bybit = 'assets'

print(all_reports.binance)