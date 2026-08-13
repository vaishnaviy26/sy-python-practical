# Student Marks Management System

students = []
marks = []

while True:
    print("\n===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")


    


    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        mark = float(input("Enter marks: "))
        students.append(name)
        marks.append(mark)
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("---------------------------")
            for i in range(len(students)):
                print(f"{i+1}. {students[i]} : {marks[i]}")

    elif choice == 3:
        name = input("Enter student name to update: ")
        if name in students:
            index = students.index(name)
            new_mark = float(input("Enter new marks: "))
            marks[index] = new_mark
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    elif choice == 4:
        name = input("Enter student name to delete: ")
        if name in students:
            index = students.index(name)
            students.pop(index)
            marks.pop(index)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == 5:
        name = input("Enter student name to search: ")
        if name in students:
            index = students.index(name)
            print("Student Name :", students[index])
            print("Marks :", marks[index])
        else:
            print("Student not found.")

    elif choice == 6:
        print("Thank you for using the Student Marks Management System!")
        break

    else:
        print("Invalid choice! Please try again.")