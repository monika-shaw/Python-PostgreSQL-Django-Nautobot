import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

# print(response.json())

print(response.status_code)
print(response.text)


#3. Get a Specific User

user_id = 5

url = url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

res = requests.get(url)

print(res.text)