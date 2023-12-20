import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Send a request to the URL
response = requests.get(url)

# Display the body of the response
print(response.text)

# Check if the HTTP status code is greater than or equal to 400
if response.status_code >= 400:
    print("Error code:", response.status_code)