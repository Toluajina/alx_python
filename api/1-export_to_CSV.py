"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

def export_employee_tasks_to_csv(employee_id):
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url_user)
    if user_response.status_code != 200:
        print(f"Failed to retrieve user data for user with ID {employee_id}.")
        return
    
    user_data = user_response.json()
    username = user_data['username']
    
    url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(url_todos)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve todos for user with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()
    
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': 'Completed' if todo['completed'] else 'Not Completed',
                'TASK_TITLE': todo['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    export_employee_tasks_to_csv(employee_id)