import sys
import json
import requests


def export_to_json(employee_id):
    # Retrieve employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Retrieve employee's todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Prepare data in JSON format
    json_data = {
        "USER_ID": [
            {"task": task['title'], "completed": task['completed'], "username": username} for task in todo_data
        ]
    }

    # Write data to JSON file
    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump(json_data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
