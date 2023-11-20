

class Exchanges:
    market = None # будем выводить Spot или Futures  
    usdt = None # обращается ли на бирже 
    russia = None # действует ли в РФ

    def futures(self):  
        return f"{self.market} futures" # 

    def spot(self):  
        return f"{self.market} spot" # 


report = Exchanges()
report.market = 'Рынок:'

print(report.futures())