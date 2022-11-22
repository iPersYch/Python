from API.API_request import get_response

# Проверяем статус код на ОК 200
def test_status_code():
    status_code = get_response().status_code
    assert status_code == 200, "Status code should be 200"

# Проверяем, что ответ с нужным параметром
def test_get_with_params():
    name = 'Вадим'
    response_dict = get_response(params={'name': name})
    assert response_dict.json()['answer'] == f'Hello, {name}', f"Wrong answer, should be {name} in response'"
