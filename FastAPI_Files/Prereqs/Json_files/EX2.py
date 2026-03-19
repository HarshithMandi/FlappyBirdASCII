import json

with open("Prereqs/Json_files/user.json","r") as file:
    data=json.load(file)

print(data["name"])

