import requests
import pprint #библиотека которая позволяет структурно выводить данные  

tickers = requests.get("https://api.binance.com/api/v3/ticker/24hr")
#создали переменную tickers, с в которую с помощью 
#библиотеки requests написанную до нас
#использовали метод get, который отправил запрос на биржу по ссылке. в зависимости от задачи ссылка разная 

result = tickers.json()
pprint.pprint(result)

# pprint.pprint(result[0])
# print(result)

