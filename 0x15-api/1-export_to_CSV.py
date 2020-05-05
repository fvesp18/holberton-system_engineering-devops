#!/usr/bin/python3
""" Script will make request to website and format response """
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    # Make request
    emp_req = requests.get("{}users/{}".format(
        "https://jsonplaceholder.typicode.com/", sys.argv[1]))
    todo_req = requests.get("{}users/{}/todos".format(
        "https://jsonplaceholder.typicode.com/", sys.argv[1]))

    # Specify field desired and add counter
    username = emp_req.json().get('username')
    user_id = emp_req.json().get('id')
    todo = todo_req.json()

    # Write to file using csv writer
    with open("{}.csv".format(sys.argv[1]), mode="w") as csvFile:
        task_writer = csv.writer(csvFile, delimiter=",",
                                 quotechar='"', quoting=csv.QUOTE_ALL)

        for tasks in todo:
            task_writer.writerow([
                user_id,
                username,
                tasks.get('completed'),
                tasks.get('title')])
