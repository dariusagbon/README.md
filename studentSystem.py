import csv

students = []

def load_students(filename='students.csv'):
    global students
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]  
    except FileNotFoundError:
        students = []

def save_students(filename='students.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

def add_student(name, age, grade):
    student_id = len(students) + 1
    students.append({'id': student_id, 'name': name, 'age': age, 'grade': grade})
    save_students()
    print(f"Student {name} added with ID {student_id}.")

def view_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def update_student(student_id, name=None, age=None, grade=None):
    global students
    for student in students:
        if student['id'] == str(student_id):
            if name:
                student['name'] = name
            if age:
                student['age'] = age
            if grade:
                student['grade'] = grade
            save_students()
            print(f"Student ID {student_id} updated.")
            return

    print(f"Student ID {student_id} not found.")
    return

def delete_student(student_id):
    global students
    for i, student in enumerate(students):
        if student['id'] == str(student_id):
            del students[i]
            save_students()
            print(f"Student ID {student_id} deleted.")
            return
    print(f"Student ID {student_id} not found.") 

def main():
    load_students()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            grade = input("Enter new grade (leave blank to keep current): ")
            update_student(student_id, name or None, age or None, grade or None)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
    print("Exiting Student Management System.")
if __name__ == "__main__":
    main()
# studentSystem.py

