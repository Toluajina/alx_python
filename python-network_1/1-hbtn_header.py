import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("No X-Request-Id found in the response headers.")
else:
    print("Error: Unable to fetch the URL. Status code:", response.status_code)