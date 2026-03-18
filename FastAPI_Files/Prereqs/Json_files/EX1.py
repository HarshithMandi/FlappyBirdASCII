import json

student = {
    "name":"harshith",
    "courses":["math","physics"]
}


print(student)

json_str= json.dumps(student)
print(json_str)
print(type(json_str))
student_copy=json.loads(json_str)
print(student_copy)
print(type(student_copy))
