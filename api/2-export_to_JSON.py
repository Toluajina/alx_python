"""
Check student JSON output
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check user info """
    
    with open(str(id) + '.json', 'r') as f:
        student_json = json.load(f)

    if student_json.get(str(id)) and len(student_json) == 1:
        print("Correct USER_ID: OK")
    else:
        print("Correct USER_ID: Incorrect")

    if isinstance(student_dicts, list) and all(isinstance(item, dict) for item in student_dicts):
        print("USER_ID's value type is a list of dicts: OK")
    else:
        print("USER_ID's value type incorrect")


    for i in response:
        if i['userId'] == id:
            usr_resp = requests.get(users_url + str(i['userId'])).json()
            json_entry = {'username': usr_resp[0]['username'], 'completed': i['completed'], 'task': i['title']}
            json_count += 1
            flag = 0
            for item in student_dicts:
                if json_entry == item:
                    flag = 1
            if flag == 0:
                not_found_count += 1

    if not_found_count != 0:
        print("Number of tasks missing: {}".format(not_found_count))
    else:
        print("All tasks found: OK")

if __name__ == "__main__":
    user_info(int(sys.argv[1]))