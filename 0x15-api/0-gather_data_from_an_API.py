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
        user_r = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
        todo_r = requests.get("https://jsonplaceholder.typicode.com/todos/?userId={}".format(user_id))
        print(user_r.json())
        print('---------------')
        print(todo_r.json())
