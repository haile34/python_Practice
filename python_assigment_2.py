# this is function to register student
def register_student():
    try:
        print(" Student Registration Form ")
        num_students = int(input("Enter the number of students: "))
        with open("student_info_db.txt", 'a+') as file:
            for i in range(num_students):
                st_id = input("Enter student id: ")
                file.seek(0)
                for line in file:
                    if st_id in line:
                        print("The ID already exists. Please enter a new ID...")
                        st_id = input("Enter student id: ")

                while True:
                    st_name = input("Enter student name: ")
                    if not st_name.isdigit():  
                        break
                    else:
                        print("Please enter a valid student name.")
                while True:
                    try:
                        st_gpa = float(input("Enter student GPA (between 0 and 4): "))
                        if 0 <= st_gpa <= 4:
                            break
                        else:
                            print("Please enter a valid GPA (between 0 and 4)...")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for GPA.")

                while True:
                    st_dep = input("Enter the department: ")
                    if not st_dep.isdigit():
                        break
                    else:
                        print("Invalid department name. Please enter a valid department.")

                while True:
                    
                  st_gen = input("Enter student gender: ")
                  if not st_gen.isdigit():
                       break
                  else:
                        print("Invalid input. Please enter a valid m/f.")
                       
                file.write(f"{st_id};{st_name};{st_gen};{st_dep};{st_gpa}\n")
                print("Registered successfully.")

        print("*__*__*__*__*__*__*__*__*__*__*__*")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()

# to search a student using ID 
def search_student():
    try:
        found = False
        id_search = input("Enter student ID: ")
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if stid == id_search:
                    print("____student found____")
                    print(f"Name: {name}\nGender: {gender}\nDepartment: {dep}\nGPA: {gpa}")
                    found = True
                    break
            if not found:
                print("Student does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()
# Update student name
def update_name():
    try:
        st_id = input("Enter student ID: ")
        lines = []
        modified = False

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if st_id == stid:
                
                    while True:
                        new_name = input("Enter corrected New Name: ")
                        if not new_name.isdigit():  
                            break
                        else:
                            print("Please enter a valid student name.")
                    line = f"{stid};{new_name};{gender};{dep};{gpa}"
                    modified = True
                    print(f"Data of student {st_id} updated successfully!")
                lines.append(line)
        if not modified:
            print(f"Student with ID {st_id} not found.")
        else:
            with open("student_info_db.txt", 'w') as file:
                file.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()

# update student GPA
def update_gpa():
    try:
        st_id = input("Enter student ID: ")
        updated = False
        lines = []

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if st_id == stid:
                    while True:
                        try:
                            new_gpa = float(input("Enter corrected New GPA (between 0 and 4): "))
                            if 0 <= new_gpa <= 4:
                                break
                            else:
                                print("Please enter a valid GPA (between 0 and 4)...")
                        except ValueError:
                            print("Invalid input. Please enter a numeric value for GPA.")
                    line = f"{stid};{name};{gender};{dep};{new_gpa}\n"
                    updated = True
                    print(f"Data of student {name} updated successfully!")
                lines.append(line)
        if not updated:
            print(f"Student with ID {st_id} not found.")
        else:
            with open("student_info_db.txt", 'w') as file:
                file.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()

# show all student
def show_all():
    try:
        print("Student database:\n")
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                print(f"ID: {stid}\nName: {name}\nGender: {gender}\nDepartment: {dep}\nGPA: {gpa}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu() 
       
# to delete student information
def delete_student():
    try:
        st_id = input("Enter student ID to delete: ")
        found = False
        lines = []

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.strip().split(";")
                if st_id != stid:
                    lines.append(line)
                else:
                    found = True
                    print(f"Student with ID {st_id} deleted successfully.")

        if not found:
            print(f"Student with ID {st_id} not found.")

        with open("student_info_db.txt", 'w') as file:
            file.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# total student in the database
def total_students():
    try:
        total = 0
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                total += 1
        print(f"Total number of students: {total}")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# total number of students based on gender
def total_num_based_gen():
    try:
        total = 0
        students_gender = input("Input Student Gender (m/f): ")
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if gender.lower() == students_gender.lower():
                    total += 1
        print(f"Total number of students ({students_gender}): {total}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    menu()

# top scoring student in department
def top_students_per_department():
    try:
        with open("student_info_db.txt", "r") as file:
            st_dep = input("Enter the department: ").lower()
            max_gpa = 0
            max_name = ""
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                dep = dep.lower()
                if dep == st_dep and float(gpa) > max_gpa:
                    max_gpa = float(gpa)
                    max_name = name

            if max_name:
                print(f"Top scoring student in {st_dep} department: {max_name} with GPA {max_gpa}")
            else:
                print(f"No student found in {st_dep} department.")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()


# top scoring women student
def top_scoring_women_department():
    try:
        with open("student_info_db.txt", "r") as file:
            st_dep = input("Enter the department: ").lower()
            max_gpa = 0
            max_name = ""
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                dep = dep.lower()
                if dep == st_dep and float(gpa) > max_gpa and gender.lower() == "female":
                    max_gpa = float(gpa)
                    max_name = name
            if max_name:
                print(f"Top scoring female student in {st_dep} department is: {max_name} with GPA {max_gpa}")
            else:
                print(f"No female student found in {st_dep} department.")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# search student based on GPA
def stu_based_on_gpa():
    try:
        found_student = []
        search_stu_gpa = float(input("Enter Students GPA: "))
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stuid, stname, stgender, stdep, stgpa = line.split(";")
                stgpa = float(stgpa)
                if stgpa == search_stu_gpa:
                    found_student.append((stuid, stname, stgender, stdep, stgpa))
        if found_student:
            for student in found_student:
                stuid, stname, stgender, stdep, stgpa = student
                print(f"ID: {stuid}\nName: {stname}\nGender: {stgender}\nDepartment: {stdep}\n")
        else:
            print("There is no student with this GPA.")
    except Exception as e:
        print(f"An error occurred: {e}")


    menu()

# Frequent name
def used_name():
    try:
        name_count = {}
        with open("student_info_db.txt", "r") as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if name in name_count:
                    name_count[name] += 1
                else:
                    name_count[name] = 1
            for name, count in name_count.items():
                print(f"{name} : is frequented {count} times\n")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()

# Function to show number of students per department
def students_per_department():
    try:
        department_counts = {}
        
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                department_counts[dep] = department_counts.get(dep, 0) + 1
        
        print("Number of students per department:")
        for department, count in department_counts.items():
            print(f"{department}: {count}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    menu()

# students that above to the given GPA
def above_agiven_GPA():
    try:
        st_gpa = float(input("Enter the GPA threshold: "))
        top_students = []

        with open("student_info_db.txt", "r") as file:
            for line in file:
                stid, name, gender, dep, gpa = line.strip().split(";")
                if float(gpa) > st_gpa:
                    top_students.append((name, gpa))

        if top_students:
            print(f"Top scoring students with GPA greater than {st_gpa}:")
            for name, gpa in top_students:
                print(f"{name} with GPA {gpa} in {dep} Department")
        else:
            print(f"No students found with GPA greater than {st_gpa}")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()
# top scoring women student in the each department
def top_scoring_women_department():
    try:
        with open("student_info_db.txt", "r") as file:
            st_dep = input("Enter the department: ")
            top_gpa = 0
            max_name = ""
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if dep == st_dep and float(gpa) > top_gpa and gender.lower() == "female":
                    top_gpa = float(gpa)
                    max_name = name
            if max_name:
                print(f"Top female student in {st_dep} department is: {max_name} with GPA {top_gpa}")
            else:
                print(f"No female student found in {st_dep} department.")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()


# main function
def menu():
    print(">>>>>>>>>>>>>>>>>>>>>>>Student Management System<<<<<<<<<<<<<<<<<<<<<<")
    print("1. Register new student")
    print("2. Search Student")
    print("3. Update Student Name")
    print("4. Update Student GPA")
    print("5. Display All Students")
    print("6. Delete Student Information")
    print("7. Total Number of Students")
    print("8. Total Number of Students based on Gender")
    print("9. Top Scoring Students")
    print("10. Top Scoring Women Students")
    print("11. Search Students grater than a given GPA")
    print("12. Display Frequent Student Name")
    print("13. Students per Department")
    print("14. EXIT")
    
    choice = input("Enter your choice (1-14): ")
    
    try:
        choice = int(choice)
        if choice == 1:
            register_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            update_name()
        elif choice == 4:
            update_gpa()
        elif choice == 5:
            show_all()
        elif choice == 6:
            delete_student()
        elif choice == 7:
            total_students()
        elif choice == 8:
            total_num_based_gen()
        elif choice == 9:
            top_students_per_department()
        elif choice == 10:
           top_scoring_women_department()
        elif choice == 11:
            above_agiven_GPA()
        elif choice == 12:
            used_name()
        elif choice == 13:
            students_per_department()
        elif choice == 14:
            exit_program()
        else:
            print("Invalid choice! Please enter a number between 1 and 14.")
         
    except ValueError:
        print(">>>Please enter a number between 1 and 14<<<<<")
    
        
# exiting program
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

menu()


