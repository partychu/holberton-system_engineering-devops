#!/usr/bin/python3
"""
 Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) == 1:
        pass
    else:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/todos/?userId={}"

        user_j = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                              .format(user_id)).json()
        todo_j = requests.get(url.format(user_id)).json()

        data_list = []
        for t in todo_j:
            data = [user_id, user_j.get('username'),
                    t.get('completed'), t.get('title')]
            data_list.append(data)
        with open("{}.csv".format(user_id), 'w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(data_list)
