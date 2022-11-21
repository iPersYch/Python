import requests

response_valid = requests.get('https://providence.kazan.startru.tech/api/v1/tasks_tracker', params={'task_type': 'VALIDATION'}).json()
print('На данный момент на валидации находятся ', len(response_valid['all']), ' задач')

response_dmca = requests.get('https://providence.kazan.startru.tech/api/v1/tasks_tracker', params={'task_type':'DMCA'}).json()
print('На данный момент на DMCA находятся ', len(response_dmca['all']), ' задач')