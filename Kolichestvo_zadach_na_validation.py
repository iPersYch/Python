import requests

response = requests.get('https://providence.kazan.startru.tech/api/v1/tasks_tracker', params={'task_type':'VALIDATION'}).json()
print('На данный момент на валидации находится ', len(response['all']), ' задач')
