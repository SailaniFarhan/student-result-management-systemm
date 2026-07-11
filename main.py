print("STUDENT RESULT MANAGEMENT SYSTEM")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        maths = float(input("Enter marks in Maths: "))
        science = float(input("Enter marks in Science: "))
        english = float(input("Enter marks in English: "))

        total = maths + science + english
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        student = {
            "name": name,
            "roll_no": roll_no,
            "maths": maths,
            "science": science,
            "english": english,
            "total": total,
            "percentage": percentage,
            "grade": grade,
        }

        students.append(student)
        print("Student added successfully")

    elif choice == "2":
        search_roll_no = input("Enter student roll number: ")
        found = False

        for student in students:
            if student["roll_no"] == search_roll_no:
                found = True
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Maths Marks:", student["maths"])
                print("Science Marks:", student["science"])
                print("English Marks:", student["english"])
                print("Total Marks:", student["total"])
                print("Percentage:", student["percentage"])
                print("Grade:", student["grade"])
                break

        if not found:
            print("Student not found")

    elif choice == "3":
        if len(students) == 0:
            print("No students available")
        else:
            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Maths Marks:", student["maths"])
                print("Science Marks:", student["science"])
                print("English Marks:", student["english"])
                print("Total Marks:", student["total"])
                print("Percentage:", student["percentage"])
                print("Grade:", student["grade"])
                print("-" * 20)

    elif choice == "4":
        search_roll_no = input("Enter student roll number to search: ")
        found = False

        for student in students:
            if student["roll_no"] == search_roll_no:
                found = True
                print("Student found:", student["name"])
                break

        if not found:
            print("Student not found")

    elif choice == "5":
        print("Exiting the system")
        break

    else:
        print("Invalid choice")

