

import requests


API_KEY = '2nMcl8cfqOmDHSFlz3'
SECRET_KEY = 'izdBWtSxvqeD04q9t3wTNMzFJ61KKVDwoDIi'
BASE_URL = 'https://api.bybit.com'

# Формируем параметры запроса
params = {
    'api_key': API_KEY,
}

# Выполняем GET-запрос к эндпоинту /v2/private/account/get-account
response = requests.get(f'{BASE_URL}/v2/private/account/get-account', params=params)

# Проверяем код ответа
if response.status_code == 200:
    # Получаем данные об аккаунте
    account_data = response.json()
    # Печатаем информацию об аккаунте
    print(account_data)
else:
    print('Ошибка при выполнении запроса:', response.status_code)