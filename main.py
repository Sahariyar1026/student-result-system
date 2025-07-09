students = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    students[name] = marks

def show_students():
    for name, marks in students.items():
        print(f"{name}: {marks}")

while True:
    print("\n1. Add Student\n2. Show Students\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
