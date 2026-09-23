import requests

url = "http://localhost:8080/api/dcim/devices/"

headers = {
    "Authorization": "Token 163aa20aa1ab2d281260f2da5dc6a7c6ff94bbec"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())