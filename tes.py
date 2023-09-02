import requests



url = 'https://mos-sud.ru/territorial'  # замените на фактический URL запроса
params = {'q': 'Москва, Химкинский бульвар, 3, подъезд 3' }  # параметры запроса
response = requests.get(url, params=params)
print(response)