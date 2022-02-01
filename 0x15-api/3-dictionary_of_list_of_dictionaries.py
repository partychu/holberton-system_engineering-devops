#!/usr/bin/python3
"""
 Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    url_au = "https://jsonplaceholder.typicode.com/users"
    all_users_j = requests.get(url_au).json()
    max_user_id = len(all_users_j)
    user_id = 1
    j_dict = {}

    for i in range(max_user_id):
        url_u = "https://jsonplaceholder.typicode.com/users/{}"
        url_t = "https://jsonplaceholder.typicode.com/todos/?userId={}"

        user_j = requests.get(url_u.format(user_id)).json()
        todo_j = requests.get(url_t.format(user_id)).json()

        value_list = []
        for t in todo_j:
            nested_dict = {}
            nested_dict["username"] = user_j.get('username')
            nested_dict["task"] = t.get('title')
            nested_dict["completed"] = t.get('completed')
            value_list.append(nested_dict)
        j_dict[user_id] = value_list
        user_id += 1
    with open("todo_all_employees.json", 'w', newline='') as f:
        json.dump(j_dict, f)
