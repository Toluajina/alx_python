"""
This script exports TODO list data for a given employee from a REST API to a JSON file.

Requirements:
- The script accepts an integer as a parameter, which is the employee ID.
- It retrieves information about tasks owned by the employee from the API.
- It exports the data in JSON format.
- The output file format is USER_ID.json.

Usage:
python3 script_name.py <employee_id>
"""

import sys
import json
import requests


def export_to_json(employee_id):
    """
    Export TODO list data for the given employee to a JSON file.

    Args:
        employee_id (int): The ID of the employee whose TODO list data is to be exported.

    Returns:
        None
    """
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
