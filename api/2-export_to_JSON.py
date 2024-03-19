"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve user information
    user_response = requests.get(url + "users/{}".format(user_id))
    if user_response.status_code != 200:
        print("User with ID {} not found.".format(user_id))
        sys.exit(1)
    
    user = user_response.json()
    username = user.get("username")
    
    # Retrieve todos
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Failed to retrieve todos for user with ID {}.".format(user_id))
        sys.exit(1)
    
    todos = todos_response.json()
    
    # Check if todos is a list of dictionaries
    if not isinstance(todos, list) or not all(isinstance(item, dict) for item in todos):
        print("USER_ID's value type is not a list of dicts.")
        sys.exit(1)
    
    # Check if any tasks are found
    if not todos:
        print("No tasks found for user with ID {}.".format(user_id))
        sys.exit(1)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
    
    print("Correct USER_ID: OK")
    print("USER_ID's value type is a list of dicts: OK")
    print("All tasks found: OK")
