#!/usr/bin/python3
""" Script will make request to website and format response """
if __name__ == "__main__":
    import json
    import requests
    import sys

    # Make request
    emp_req = requests.get("{}users/{}".format(
        "https://jsonplaceholder.typicode.com/", sys.argv[1]))
    todo_req = requests.get("{}users/{}/todos".format(
        "https://jsonplaceholder.typicode.com/", sys.argv[1]))

    # Specify field desired and add counter
    emp_name = emp_req.json().get('name')
    todo = todo_req.json()
    total_tasks = 0
    comp_tasks = 0

    # Iterate through tasks, make total count and completed count
    for tasks in todo:
        total_tasks += 1
        if tasks.get('completed'):
            comp_tasks += 1

    # Format data and print
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, comp_tasks, total_tasks))
    for tasks in todo:
        if tasks.get('completed'):
            print("\t {}".format(tasks.get('title')))
