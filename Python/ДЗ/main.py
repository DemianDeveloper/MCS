ltcusdt = 70.01
maticusdt = 0.6506
rndrusdt = 2.163
filusdt = 3.827
tonusdt = 2.1828

def get_summa_activa():
    summa = ltcusdt + maticusdt + rndrusdt + filusdt + tonusdt
    print(summa)
    return summa

summa_a = get_summa_activa()
balance = 77

def get_raznica_is_balansa():
    minus = balance - summa_a
    print(minus)

get_raznica_is_balansa()