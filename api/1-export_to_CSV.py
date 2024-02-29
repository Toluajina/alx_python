import csv
import requests
import sys


def get_employee_info(employee_id):
    # Retrieve employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']
    user_id = employee_data['id']
    username = employee_data['username']

    # Retrieve employee's todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Prepare CSV data
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in todo_data:
        csv_data.append([user_id, username, task['completed'], task['title']])

    # Write data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f"CSV file '{filename}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)