employee={
    {
        "name":"John",
        "age":30,
        "department":"HR",
        "salary":50000
    },
    {
        "name":"Alice",
        "age":28,
        "department":"IT",
        "salary":60000
    },
    {
        "name":"Bob",
        "age":35,
        "department":"Finance",
        "salary":55000
    },
    {
        "name":"Eve",
        "age":32,
        "department":"Marketing",
        "salary":52000
    }   

}

remove_employee=input("Enter the name of the employee to remove: ")
employee = [emp for emp in employee if emp["name"] != remove_employee]
print(f"Employee {remove_employee} removed.")
print(employee)


copy_employee=employee.copy()

"""
check whether employee exists in the list"""
if copy_employee:
    print("Employee exists in the list.")
else:
    print("Employee does not exist in the list.")


    """
    clear the list of employees"""
employee.clear()
print("Employee list cleared.")
print(employee)