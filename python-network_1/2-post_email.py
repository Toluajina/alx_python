import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Send a POST request with the email as a parameter
response = requests.post(url, data={'email': email})

# Display the body of the response
print(response.text)