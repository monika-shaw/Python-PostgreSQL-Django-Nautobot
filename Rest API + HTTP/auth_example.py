import requests

username = "monika"
password = "mypassword"

response = requests.get(
    "https://example.com/users",
    auth=(username, password),
    timeout=5
)

print(response.status_code)