#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list

import requests as r
from sys import argv
if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(argv[1])).json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                  .format(argv[1])).json()
    done = []
    for task in tasks:
        if task.get('completed') is True:
            done.append(task)
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(done), len(tasks)))
    for task in done:
        print('\t ' + task.get('title'))
