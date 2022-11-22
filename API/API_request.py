import requests

# Получает заголовки ответа и запроса

response = requests.get('https://playground.learnqa.ru/api/show_all_headers')
print(response.text)
print(response.headers)

# Получает Cookies ответа и выводит его

payload = {'login':'secret_login', 'password':'secret_pass'}
response = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(response.headers)

# Получае куку сохраняем ее в переменную, проводит регистрацию с помощью это куки во втором запросе

payload = {'login':'secret_login', 'password':'secret_pass'}
response1 = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
response1_cookie= response1.cookies.get('auth_cookie')
cookies= {}
if response1_cookie is not None:
    cookies.update({'auth_cookie': response1_cookie})
response2 = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=cookies)
print(response2.text)

