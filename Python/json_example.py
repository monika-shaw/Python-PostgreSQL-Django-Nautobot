import json

with open("devices.json","r") as file:
    content = json.load(file)

print(content)

for device in content["devices"]:
    print(device["name"])
    print(device["details"]["ip"])
    print(device["details"]["status"])