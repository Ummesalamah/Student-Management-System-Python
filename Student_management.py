import json
students = []
def menu():
    print("====== STUDENT MANAGEMENT SYSTEM ======\n" \
    "1. Add Student\n" \
    "2. Display Student\n" \
    "3. Search Student\n" \
    "4. Update Student\n" \
    "5. Delete Student\n" \
    "6. Exit\n")
def save_students():
    with open("students.json","w") as file:
        json.dump(students, file, indent = 4)
def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    except json.JSONDecodeError:
        students = []
def add_students():

    # Admission No.
    try:
        admission_no = int(input("Enter Admission No.: "))
    except ValueError:
        print("❌ Invalid Admission Number!")
        return

    if admission_no <= 0:
        print("❌ Admission Number must be greater than 0!")
        return

    # Duplicate Admission No.
    for student in students:
        if student["Admission No."] == admission_no:
            print("❌ Admission Number already exists!")
            return

    # Name
    name = input("Enter Student Name: ").strip()

    if name == "":
        print("❌ Name cannot be empty!")
        return

    if not name.replace(" ", "").isalpha():
        print("❌ Name should contain only alphabets!")
        return

    # Standard
    try:
        standard = int(input("Enter Class (1-12): "))
    except ValueError:
        print("❌ Invalid Standard!")
        return

    if standard < 1 or standard > 12:
        print("❌ Standard must be between 1 and 12!")
        return

    # Roll No.
    try:
        roll_no = int(input("Enter Roll No.: "))
    except ValueError:
        print("❌ Invalid Roll Number!")
        return

    if roll_no <= 0:
        print("❌ Roll Number must be greater than 0!")
        return

    # Duplicate Roll No. in Same Class
    for student in students:
        if student["Standard"] == standard and student["Roll No."] == roll_no:
            print("❌ Roll Number already exists in this class!")
            return

    # Contact
    contact = input("Enter Contact Number: ").strip()

    if len(contact) != 10 or not contact.isdigit():
        print("❌ Contact Number must contain exactly 10 digits!")
        return

    if contact[0] not in "6789":
        print("❌ Contact Number should start with 6, 7, 8 or 9!")
        return

    # Address
    address = input("Enter Address: ").strip()

    if address == "":
        print("❌ Address cannot be empty!")
        return

    # Student Dictionary
    student = {
        "Admission No.": admission_no,
        "Name": name.title(),
        "Standard": standard,
        "Roll No.": roll_no,
        "Contact": contact,
        "Address": address.title()
    }

    students.append(student)
    save_students()

    print("\n✅ Student Added Successfully!")
    print("-----------------------------")
    display_students(student)
def display_students(student):
    print("Admission No. : ",student["Admission No."])
    print("Name : ",student["Name"])
    print("Standard : ",student["Standard"])
    print("Roll No. : ",student["Roll No."])
    print("Contact : ",student["Contact"])
    print("Address : ",student["Address"])
def display_students_all():
    if not students:
        print("No students detail found")
    else:
        for i, student in enumerate(students, start=1):
            print("----------------------")
            print(f"Student {i}")
            print("----------------------")
            display_students(student)
            print("----------------------")
def search_students():
    print("== SEARCH OPTIONS ==\n" \
    "1. Search by Admission No.\n" \
    "2. Search by Name\n" \
    "3. Search by Roll No. and Standard\n")
    try:
        option = int(input("Enter search option : "))
    except ValueError:
        print("❌ Invalid Option!")
        return
    
    if option == 1:
        try:
            admission_search = int(input("Enter Admission Number: "))
        except ValueError:
            print("❌ Invalid Admission Number!")
            return
        found = False
        for student in students:
            if student["Admission No."] == admission_search:
                display_students(student)
                found = True
                break
        if not found:
                print("Student not found!")
    elif option == 2:
        name_search = str(input("Enter Name to Search: "))
        found = False
        for student in students:
            if name_search.lower() in student["Name"].lower():
                display_students(student)
                found = True
                break
        if not found:
                print("Student not found!")
    elif option == 3:
        try:
            roll_search = int(input("Enter Roll No. to Search: "))
            standard_search = int(input("Enter Standard to Search: "))
        except ValueError:
            print("❌ Invalid Input!")
            return
        found = False
        for student in students:
            if student["Roll No."] == roll_search and student["Standard"] == standard_search:
                display_students(student)
                found = True
                break
        if not found:
                print("Student not found!")
    else:
        print("Invalid Option")
def update_students():
    try:
        admission_search = int(input("Enter Admission Number: "))
    except ValueError:
        print("❌ Invalid Admission Number!")
        return

    found = False
    for student in students:
        if student["Admission No."] == admission_search:
            display_students(student)
            print("== UPDATE OPTIONS ==\n"
                  "1. Update Name\n"
                  "2. Update Standard\n"
                  "3. Update Roll No.\n"
                  "4. Update Contact\n"
                  "5. Update Address\n")

            try:
                update = int(input("Enter Update Option : "))
            except ValueError:
                print("❌ Invalid Option!")
                return
            
            if update == 1:
                new_name = input("Enter New Name: ").strip()
                if new_name == "":
                    print("❌ Name cannot be empty!")
                    return
                if not new_name.replace(" ", "").isalpha():
                    print("❌ Name should contain only alphabets!")
                    return
                student["Name"] = new_name.title()

            elif update == 2:
                try:
                    new_standard = int(input("Enter New Standard: "))
                except ValueError:
                    print("❌ Invalid Standard!")
                    return
                if new_standard < 1 or new_standard > 12:
                    print("❌ Standard must be between 1 and 12!")
                    return
                student["Standard"] = new_standard

            elif update == 3:
                try:
                    new_rollno = int(input("Enter New Roll No.: "))
                except ValueError:
                    print("❌ Invalid Roll Number!")
                    return
                if new_rollno <= 0:
                    print("❌ Roll Number must be greater than 0!")
                    return

                # Duplicate Roll No. in same class
                for s in students:
                    if s != student and s["Standard"] == student["Standard"] and s["Roll No."] == new_rollno:
                        print("❌ Roll Number already exists in this class!")
                        return

                student["Roll No."] = new_rollno

            elif update == 4:
                new_contact = input("Enter New Contact: ").strip()
                if len(new_contact) != 10 or not new_contact.isdigit():
                    print("❌ Contact Number must contain exactly 10 digits!")
                    return
                if new_contact[0] not in "6789":
                    print("❌ Contact Number should start with 6, 7, 8 or 9!")
                    return
                student["Contact"] = new_contact

            elif update == 5:
                new_address = input("Enter New Address: ").strip()
                if new_address == "":
                    print("❌ Address cannot be empty!")
                    return
                student["Address"] = new_address.title()

            else:
                print("❌ Invalid Choice!")
                return

            save_students()
            print("✅ Student Updated Successfully!")
            display_students(student)
            found = True
            break
    if not found:
        print("❌ Student not found!")
def delete_students():
    try:
        admission_search = int(input("Enter Admission Number: "))
    except ValueError:
        print("❌ Invalid Admission Number!")
        return
    found = False
    for student in students:
        if student["Admission No."] == admission_search:
            display_students(student)
            confirm = input("Are you sure you want to delete this student? (Y/N): ").upper()
            if confirm == "Y":
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
                found = True
                break
            elif confirm == "N":
                print("Deletion Cancelled!")
                break
            else:
                print("Invalid Choice!")
                break
    if not found:
        print("Student not found!")

load_students()
choice = 0
while choice != 6:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid Input! Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        #add students
        add_students()
    elif choice == 2:
        #display students
        display_students_all()
    elif choice == 3:
        #search students
        search_students()
    elif choice == 4:
        #update students
        update_students()
    elif choice == 5:
        #delete students
        delete_students()
    elif choice == 6:
        save_students()
        print("Thank you for using Student Management System!")
    else:
        print("invalid choice")