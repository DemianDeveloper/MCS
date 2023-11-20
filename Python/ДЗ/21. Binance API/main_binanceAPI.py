'''
https://github.com/binance/binance-futures-connector-python
установить библиотеку:
pip install binance-futures-connector

регистрация кабинета WLC - 25% возврат комиссий:
https://passport.whitelist.capital/signup/MTAx:1qY3wq:aV_75UsXV64R63uafwmSbvG4PwLqwP0uSnOZXCybrz0/
'''

from binance.um_futures import UMFutures
import pprint

client = UMFutures(key='---', secret='---')



def get_balance():
    balance = client.balance()


def open_market_order(symbol, side, quantity):
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'MARKET',
        'quantity': quantity,
    }

    response = client.new_order(**params)
    print(response)
# open_market_order('THETAUSDT', 'BUY', 11)    


def open_limit_order(symbol, side, quantity, price):
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price
    }

    response = client.new_order(**params)
    print(response)


def stop_order(symbol, side, price, quantity):
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'STOP_MARKET',
        # 'timeInForce': 'GTC',
        'stopPrice': price,
        'quantity': quantity,
    }

    response = client.new_order(**params)
    print(response)

stop_order('THETAUSDT', 'SELL', 0.5850,)
# open_limit_order('THETAUSDT', 'BUY', 11, 0.5840)

def cancel_open_orders(symbol):
    client.cancel_open_orders(symbol, recvWindow=2000)



