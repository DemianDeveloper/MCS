import requests

url = "https://api-testnet.bybit.com/v5/account/wallet-balance"

payload={}
headers = {
  'X-BAPI-API-KEY': '2nMcl8cfqOmDHSFlz3',
  'X-BAPI-TIMESTAMP': '1698118475428',
  'X-BAPI-RECV-WINDOW': '20000',
  'X-BAPI-SIGN': '****'#сюда добавил свой secret-key 
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)