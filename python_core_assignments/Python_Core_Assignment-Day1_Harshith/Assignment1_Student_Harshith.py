students = []

def get_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 55:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ")
    while True:
        try:
            python = int(input("Enter Python marks (0-100): "))
            sql = int(input("Enter SQL marks (0-100): "))
            linux = int(input("Enter Linux marks (0-100): "))
            if all(0 <= m <= 100 for m in [python, sql, linux]):
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter valid integer marks.")
    students.append({"name": name, "python": python, "sql": sql, "linux": linux})
    print(f"Record for {name} added successfully.")

def display_all():
    if not students:
        print("No records found.")
        return
    print(f"\n{'Name':<20} {'Python':<10} {'SQL':<10} {'Linux':<10} {'Average':<10} {'Grade'}")
    print("-" * 65)
    for s in students:
        avg = (s["python"] + s["sql"] + s["linux"]) / 3
        print(f"{s['name']:<20} {s['python']:<10} {s['sql']:<10} {s['linux']:<10} {avg:<10.2f} {get_grade(avg)}")

def search_student():
    name = input("Enter student name to search: ").strip().lower()
    found = False
    for s in students:
        if s["name"].lower() == name:
            avg = (s["python"] + s["sql"] + s["linux"]) / 3
            print(f"\nName    : {s['name']}")
            print(f"Python  : {s['python']}")
            print(f"SQL     : {s['sql']}")
            print(f"Linux   : {s['linux']}")
            print(f"Average : {avg:.2f}")
            print(f"Grade   : {get_grade(avg)}")
            found = True
            break
    if not found:
        print("Student not found.")

def class_average():
    if not students:
        print("No records to calculate average.")
        return
    total = sum((s["python"] + s["sql"] + s["linux"]) / 3 for s in students)
    print(f"\nClass Average: {total / len(students):.2f}")

while True:
    print("\n===== Student Performance Analyzer =====")
    print("1. Add Student Record")
    print("2. Display All Student Records")
    print("3. Search Student by Name")
    print("4. Show Class Average")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_all()
    elif choice == '3':
        search_student()
    elif choice == '4':
        class_average()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
