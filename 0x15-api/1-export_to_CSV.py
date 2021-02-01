#!/usr/bin/python3
# script to export data in the CSV format.

import csv
import requests as r
from sys import argv
if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(argv[1])).json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                  .format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), mode='w') as f:
        file = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            file.writerow([argv[1],
                           user.get('username'),
                           task.get('completed'),
                           task.get('title')])
