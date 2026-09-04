student = {}

while True:
    print("------Student Manager App------")
    print("1. Enter student information")
    print("2. Check student Results")
    print("3. View student information")
    print("4. Exit")

    choice = input("Enter your choice: ")
    # add student information
    if choice == '1':
       name = input("Enter student name: ")
       marks = int(input('Enter marks:'))
       student[name] = marks
       print(f"{name} Successfully Added!")

    
   # check results             
    elif choice == '2':
        name = input("Enter student name: ")
        if name in student:
            marks = student[name]
            if marks >= 50:
                print("PASS")
            else:
                print("FAIL")
    elif name not in student:
        print("Student not found!")

# view student information
    elif choice == '3':
        if not student:
            print("No Student found!")

        else:
            for name, marks in student.items():
                print(name, ":", marks)
    # exit the program
    elif choice == '4':
        print("Exiting the program...")
        break
else:
    print("Invalid choice! Please try again.")
    