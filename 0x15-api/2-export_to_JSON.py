#!/usr/bin/python3
# script to export data in the JSON format.

import json
import requests as r
from sys import argv
if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(argv[1])).json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                  .format(argv[1])).json()
    data = []
    for task in tasks:
        data.append({'task': task.get('title'),
                     'completed': task.get('completed'),
                     'username': user.get('username')})
    with open('{}.json'.format(argv[1]), mode='w') as f:
        json.dump({argv[1]: data}, f)
