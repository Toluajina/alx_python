import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

# GitHub API endpoint for the authenticated user
url = 'https://api.github.com/user'

# Set up the authentication using Basic Authentication with a personal access token
auth = (username, personal_access_token)

# Send a request to the GitHub API
response = requests.get(url, auth=auth)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    user_data = response.json()
    user_id = user_data.get('id')
    print(user_id)
else:
    print("Error: Unable to fetch GitHub user information. Status code:", response.status_code)
