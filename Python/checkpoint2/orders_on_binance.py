from binance.client import Client
apikey = 'IrfDFRnaL6LO4QdcYdC1o0KXL2FCopBNy9sBkSForYd2Q1BaNfd5LCWag4azFOxZ'
secretkey = 'U9PdyJeXxtjWfSGvg4A7DcYgQfFPpfqE0AKfwT0X4ZWHZOBLL1lmPCCn5OTkpxSg'
client = Client(api_key=apikey, api_secret=secretkey)
balance = client.futures_account_balance()[6]['balance']
print(balance)
