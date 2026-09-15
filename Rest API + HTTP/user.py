import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

user_data = response.json()

print(user_data["name"])