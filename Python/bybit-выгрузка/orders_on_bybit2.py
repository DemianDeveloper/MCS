from pybit.unified_trading import HTTP

session = HTTP(
    testnet=True,
    api_key="2nMcl8cfqOmDHSFlz3",
    api_secret="izdBWtSxvqeD04q9t3wTNMzFJ61KKVDwoDIi",
)

# Получение данных о балансе кошелька
balance_data = session.get_wallet_balance(
    accountType="UNIFIED",
    coin="USDT",
)

print(balance_data)