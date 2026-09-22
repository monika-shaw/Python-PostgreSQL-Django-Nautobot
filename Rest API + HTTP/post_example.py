import requests

url = "https://jsonplaceholder.typicode.com/users"


data ={
     "name": "Monika",
    "username": "monika123",
    "email": "monika@example.com"
}

res = requests.post(url,json=data)

print(res.status_code)