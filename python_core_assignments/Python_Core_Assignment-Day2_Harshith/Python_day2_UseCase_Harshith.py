import math
import string
import random
from functools import reduce

def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

def circle_perimeter(radius):
    return round(2 * math.pi * radius, 2)

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)


cart = []

def add_item(item, price):
    cart.append({"item": item, "price": price})
    print(f"{item} added to cart.")

def remove_item(item):
    for i in cart:
        if i["item"] == item:
            cart.remove(i)
            print(f"{item} removed from cart.")
            return
    print("Item not found.")

def calculate_total():
    return sum(i["price"] for i in cart)

def process_payment(amount):
    print(f"Processing payment of Rs.{amount}...")
    if random.choice([True, False]):
        print("Payment Successful!")
    else:
        print("Payment Failed. Try again.")


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")

def reverse_string(text):
    return text[::-1]

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else s[mid]

def std_deviation(numbers):
    m = mean(numbers)
    variance = sum((x - m) ** 2 for x in numbers) / len(numbers)
    return round(variance ** 0.5, 2)

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print("File written successfully.")

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def search_in_file(filename, keyword):
    with open(filename, "r") as f:
        lines = f.readlines()
    results = [line.strip() for line in lines if keyword.lower() in line.lower()]
    return results if results else "Keyword not found."


students = []

def add_student(name, roll_no):
    students.append({"name": name, "roll_no": roll_no})
    print(f"Student {name} added.")

def view_students():
    for s in students:
        print(f"Roll No: {s['roll_no']} | Name: {s['name']}")

teachers = []

def assign_subject(name, subject):
    teachers.append({"name": name, "subject": subject})
    print(f"{name} assigned to {subject}.")

def view_teachers():
    for t in teachers:
        print(f"Teacher: {t['name']} | Subject: {t['subject']}")

def calculate_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def generate_report(name, marks):
    grade = calculate_grade(marks)
    print(f"Student: {name} | Marks: {marks} | Grade: {grade}")


accounts = {}

def create_account(acc_no, name, balance=0):
    accounts[acc_no] = {"name": name, "balance": balance}
    print(f"Account created for {name}.")

def get_balance(acc_no):
    if acc_no in accounts:
        print(f"Balance: Rs.{accounts[acc_no]['balance']}")
        return accounts[acc_no]["balance"]
    print("Account not found.")

def deposit(acc_no, amount):
    if acc_no in accounts:
        accounts[acc_no]["balance"] += amount
        print(f"Rs.{amount} deposited successfully.")
    else:
        print("Account not found.")

def withdraw(acc_no, amount):
    if acc_no in accounts:
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def transfer(from_acc, to_acc, amount):
    if from_acc in accounts and to_acc in accounts:
        if accounts[from_acc]["balance"] >= amount:
            accounts[from_acc]["balance"] -= amount
            accounts[to_acc]["balance"] += amount
            print(f"Rs.{amount} transferred successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("One or both accounts not found.")


print("===== Shapes =====")
print(circle_area(7))
print(circle_perimeter(7))
print(rectangle_area(10, 5))
print(rectangle_perimeter(10, 5))

print("\n===== Ecommerce =====")
add_item("Shoes", 1500)
add_item("Bag", 800)
remove_item("Bag")
total = calculate_total()
print(f"Total Bill: Rs.{total}")
process_payment(total)

print("\n===== Utilities =====")
print(remove_punctuation("Hello, World!"))
print(count_vowels("analytics"))
data = [10, 20, 30, 40, 50]
print(mean(data))
print(median(data))
print(std_deviation(data))
write_file("report.txt", "Sales data for Q1.\nRevenue increased by 20%.")
print(read_file("report.txt"))
print(search_in_file("report.txt", "revenue"))

print("\n===== School =====")
add_student("Ravi", 101)
add_student("Priya", 102)
view_students()
assign_subject("Mr. Kumar", "Python")
view_teachers()
generate_report("Ravi", 88)
generate_report("Priya", 63)

print("\n===== Banking =====")
create_account(1001, "Harish", 5000)
create_account(1002, "Meena", 3000)
get_balance(1001)
deposit(1001, 2000)
withdraw(1001, 1000)
transfer(1001, 1002, 500)
get_balance(1001)
get_balance(1002)

print("\n===== Lambda Functions =====")
employees = [("Asha", 85), ("Bala", 92), ("Chitra", 78)]
print(sorted(employees, key=lambda x: x[1], reverse=True))

numbers = [3, 8, 1, 6, 2, 9]
print(sorted(numbers, key=lambda x: x))

products = [("Pen", 10), ("Notebook", 50), ("Bag", 200)]
print(list(filter(lambda x: x[1] > 20, products)))

prices = [100, 200, 300]
print(list(map(lambda x: x * 0.9, prices)))

print(reduce(lambda x, y: x + y, prices))

even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 11))))
print(even_squares)
