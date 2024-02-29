import csv
import requests
import sys


def export_to_csv(employee_id):
    # Retrieve employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Retrieve employee's todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Write data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([user_id, username, task['completed'], task['title']])


def count_tasks_in_csv(employee_id):
    filename = f"{employee_id}.csv"
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            # Exclude header row
            num_tasks = sum(1 for _ in reader) - 1
            print(f"Number of tasks in CSV: {num_tasks}")
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
    count_tasks_in_csv(employee_id)
