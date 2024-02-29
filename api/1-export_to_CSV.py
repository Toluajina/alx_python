import csv
import requests
import sys


def get_employee_info(employee_id):
    # Retrieve employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)

    # Extract user ID and username
    user_id = user_data.get('id', 'Unknown')
    username = user_data.get('username', 'Unknown')

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

    # Check user ID and username
    if user_id == employee_id and username == user_data['username']:
        print("User ID and Username: OK")
    else:
        print("User ID and Username: Incorrect")

    # Check number of tasks in CSV
    num_tasks_in_csv = len(csv_data) - 1  # Subtract 1 for the header row
    num_tasks_fetched = len(todo_data)
    if num_tasks_in_csv == num_tasks_fetched:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)