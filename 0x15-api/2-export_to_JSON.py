#!/usr/bin/python3
"""
 Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import json
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

        value_list = []
        for t in todo_j:
            nested_dict = {}
            nested_dict["task"] = t.get('title')
            nested_dict["completed"] = t.get('completed')
            nested_dict["username"] = user_j.get('username')
            value_list.append(nested_dict)
        j_dict = {}
        j_dict[user_id] = value_list
        with open("{}.json".format(user_id), 'w', newline='') as f:
            json.dump(j_dict, f)

