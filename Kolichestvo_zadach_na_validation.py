import requests
import json

response = requests.get('https://providence.kazan.startru.tech/api/v1/tasks_tracker', params={'task_type':'VALIDATION'}).json()
print(len(response['all']))
