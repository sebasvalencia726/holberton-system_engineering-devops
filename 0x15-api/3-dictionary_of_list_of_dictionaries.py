#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list

import json
import requests as r
from sys import argv
if __name__ == "__main__":
    users = r.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos').json()
    data = {}
    for user in users:
        subdata = []
        for task in tasks:
            if task.get('userId') is user.get('id'):
                subdata.append({'task': task.get('title'),
                                'completed': task.get('completed'),
                                'username': user.get('username')})
        data[user.get('id')] = subdata
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data, f)
