db=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    a,b,c=input().split()
    db.append((a,b,c))    # input format is "ID Name Score"
print("add a new student")
a,b,c=input().split()
db.append((a,b,c))
print("search student name")
name=input("Enter the name to search: ")
found_students=[student for student in db if student[1]==name]
print(f"Students found with name {name}: {found_students}")
print("remove a student")
id=input("Enter the ID of the student to remove: ")
db = [student for student in db if student[0] != id]
print("Student removed.")