#!/usr/bin/python3
"""
 Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import requests
from sys import argv
import json

if __name__ == '__main__':

    if len(argv) == 1:
        pass
    else:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/todos/?userId={}"

        user_j = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                              .format(user_id)).json()
        todo_j = requests.get(url.format(user_id)).json()
        t_list = []
        for t in todo_j:
            if t.get('completed'):
                t_list.append(t.get('title'))
        print('Employee {} is done with tasks({}/{}):'
              .format(user_j.get('name'), len(t_list), len(todo_j)))
        for t in t_list:
            print('\t {}'.format(t))
