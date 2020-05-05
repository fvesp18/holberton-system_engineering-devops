#!/usr/bin/python3
if __name__ == "__main__":
    import json
    import requests
    import sys

    emp_req = requests.get("{}users/{}".format(
        "https://jsonplaceholder.typicode.com/", sys.argv[1]))
    todo_req = requests.get("{}users/{}/todos".format(
        "https://jsonplaceholder.typicode.com/", sys.argv[1]))

    emp_name = emp_req.json().get('name')
    todo = todo_req.json()
    total_tasks = 0
    comp_tasks = 0

    for tasks in todo:
        total_tasks += 1
        if tasks.get('completed'):
            comp_tasks += 1

    print("Employee {} is done with ({}/{}):".format(
        emp_name, comp_tasks, total_tasks))
    for tasks in todo:
        if tasks.get('completed'):
            print("\t{}".format(tasks.get('title')))
