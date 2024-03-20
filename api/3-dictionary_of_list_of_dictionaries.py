"""Exports to-do list information of all employees to JSON format."""
import requests
import json

def export_todo_all_employees():
    url_users = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(url_users)
    if users_response.status_code != 200:
        print("Failed to retrieve user data.")
        return
    
    users_data = users_response.json()
    todo_data = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
        if todos_response.status_code != 200:
            print(f"Failed to retrieve todos for user with ID {user_id}.")
            continue
        
        todos = todos_response.json()
        user_todos = []
        for todo in todos:
            task_title = todo['title']
            completed = todo['completed']
            user_todos.append({"username": username, "task": task_title, "completed": completed})
        
        todo_data[user_id] = user_todos
    
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data, jsonfile)

if __name__ == "__main__":
    export_todo_all_employees()
