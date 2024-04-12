# this is function to register student
def register_student():
    try:
        print(" >>>>>>>>Student Registration Form<<<<<<<<<<<<< ")
        num_students = int(input("Enter the number of students: "))
        with open("student_info_db.txt", 'a+') as file:
            for i in range(num_students):
                while True:
                    st_id = input("Enter student id: ")
                    file.seek(0)
                    id_exists = any(st_id in line for line in file)
                    if id_exists:
                        print("The ID already exists. Please enter a new ID...")
                    else:
                        break

                while True:
                    st_name = input("Enter student name: ")
                    if st_name.strip() and not st_name.isdigit():

                        break
                    else:
                        print("Please enter a valid student name.")

                while True:
                    try:
                        st_gpa_input = input("Enter student GPA (between 0 and 4): ")
                        if st_gpa_input.strip() == "":
                            print("GPA cannot be empty. Please enter a valid GPA...")
                        else:
                            st_gpa = float(st_gpa_input)
                            if 0 <= st_gpa <= 4:
                                break
                            else:
                                print("Please enter a valid GPA (between 0 and 4)...")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for GPA.")

                while True:
                    st_dep = input("Enter the department: ")
                    if st_dep.strip() and not st_dep.isdigit():
                        break
                    else:
                        print("Invalid department name. Please enter a valid department.")

                while True:
                  st_gen_input = input("Enter student gender(m/f): ")
                  st_gen = st_gen_input.strip().lower()
                  if st_gen in ('m', 'f'):
                        break
                  elif st_gen == "":
                        print("Gender cannot be empty. Please enter a valid gender (m/f)...")
                  else:
                        print("Invalid input. Please enter a valid m/f.")

                file.write(f"{st_id};{st_name};{st_gen};{st_dep};{st_gpa}\n")
                print("Registered successfully.")

        print("*__*__*__*__*__*__*__*__*__*__*__*")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()
# update GPA
def update_gpa():
    try:
        st_id = input("Enter student ID: ")
        updated = False
        lines = []

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                student = line.strip().split(";")
                if st_id == student[0]:
                    new_gpa = input("Enter new student GPA: ")
                    while True:
                        try:
                            new_gpa_float = float(new_gpa)
                            if 0 <= new_gpa_float <= 4:
                                student[4] = new_gpa
                                line = ";".join(student) + "\n"  
                                updated = True
                                print(f"GPA updated successfully for student with ID {st_id} to {new_gpa}")
                                break
                            else:
                                print("Please enter a valid GPA between 0 and 4.")
                                new_gpa = input("Enter new student GPA: ")
                        except ValueError:
                            print("Invalid input. Please enter a numeric value for GPA.")
                            new_gpa = input("Enter new student GPA: ")

                lines.append(line)

        if not updated:
            print(f"Student with ID {st_id} not found.")
        else:
            with open("student_info_db.txt", 'w') as file:
                file.writelines(lines)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

    menu()
# Function to search for a student by ID
def search_student():
    try:
        st_id = input("Enter student ID to search: ").strip()
        if not st_id:
            print("Error: Student ID cannot be empty.")
            menu()
            return

        found = False
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.strip().split(";")
                if st_id == stid:
                    found = True
                    print(f"ID: {stid}\nName: {name}\nGender: {gender}\nDepartment: {dep}\nGPA: {gpa}\n")
                    break

        if not found:
            print(f"Student with ID {st_id} not found.")
    except FileNotFoundError:
        print("Error: File 'student_info_db.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()


# Function to update student name
def update_name():
    try:
        st_id = input("Enter student ID to update name: ")
        updated = False
        lines = []

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                student = line.strip().split(";")
                if st_id == student[0]:
                    new_name = input("Enter new student name: ")
                    if new_name.strip(): 
                        student[1] = new_name
                        line = ";".join(student) + "\n"  
                        updated = True
                        print(f"Name updated successfully for student with ID {st_id} to {new_name}")
                    else:
                        print("Error: New name cannot be empty.")
                lines.append(line)

        if not updated:
            print(f"Student with ID {st_id} not found.")
        else:
            with open("student_info_db.txt", 'w') as file:
                file.writelines(lines)
    except FileNotFoundError:
        print("Error: File 'student_info_db.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()

# show all student
def show_all():
    try:
        print("Student database:\n")
        with open("student_info_db.txt", 'r') as file:
            for line in file:
                student_info = line.strip().split(";")
                if len(student_info) == 5:
                    stid, name, gender, dep, gpa = student_info
                    print(f"ID: {stid}\nName: {name}\nGender: {gender}\nDepartment: {dep}\nGPA: {gpa}\n")
                else:
                    print(f"Invalid data format in the database: {line.strip()}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# to delete student information
def delete_student():
    try:
        st_id = input("Enter student ID to delete: ").strip()
        if not st_id:
            print("Error: Student ID cannot be empty.")
            menu()
            return

        found = False
        lines = []

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                try:
                    stid, name, gender, dep, gpa = line.strip().split(";")
                except ValueError:
                    print(f"Error: Line '{line.strip()}' does not have the expected structure.")
                    continue

                if st_id != stid:
                    lines.append(line)
                else:
                    found = True
                    print(f"Student with ID {st_id} deleted successfully.")

        if not found:
            print(f"Student with ID {st_id} not found.")

        with open("student_info_db.txt", 'w') as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("Error: File 'student_info_db.txt' not found.")
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
        students_gender = input("Input Student Gender (m/f): ").strip().lower()
        total = 0

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                student_info = line.strip().split(";")
                if len(student_info) == 5:
                    stid, name, gender, dep, gpa = student_info
                    if gender.strip().lower() == students_gender:
                        total += 1
            print(f"Total number of students ({students_gender}): {total}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()


# top scoring student in department
def top_students_per_department():
    try:
        department = input("Enter the department: ").strip().lower()
        max_gpa = 0
        max_name = ""

        with open("student_info_db.txt", "r") as file:
            found = False
            for line in file:
                student_info = line.strip().split(";")
                if len(student_info) == 5:
                    stid, name, gender, dep, gpa = student_info
                    if dep.strip().lower() == department and float(gpa) > max_gpa:
                        max_gpa = float(gpa)
                        max_name = name
                        found = True

            if found:
                print(f"Top scoring student in {department.capitalize()} department: {max_name} with GPA {max_gpa}")
            else:
                print(f"No student found in {department.capitalize()} department.")
    except FileNotFoundError:
        print("File not found")
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
                try:
                    stid, name, gender, dep, gpa = line.split(";")
                    dep = dep.lower()
                    if dep == st_dep and gender.strip().lower() == "f":
                        gpa_float = float(gpa)
                        if gpa_float > max_gpa:
                            max_gpa = gpa_float
                            max_name = name
                except ValueError:
                    print(f"Error: Invalid data format in line: ")

            if max_name:
                print(f"Top scoring female student in {st_dep} department is: {max_name} with GPA {max_gpa}")
            else:
                print(f"No female student found in {st_dep} department.")
    except FileNotFoundError:
        print("Error: File 'student_info_db.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# Frequent name
def used_name():
    try:
        name_count = {}
        with open("student_info_db.txt", "r") as file:
            for line in file:
                student_info = line.strip().split(";")
                if len(student_info) == 5:
                    stid, name, gender, dep, gpa = student_info
                    if name in name_count:
                        name_count[name] += 1
                    else:
                        name_count[name] = 1
            for name, count in name_count.items():
                print(f"{name} : is frequented {count} times\n")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()


# Function to show number of students per department
def students_per_department():
    try:
        department_counts = {}

        with open("student_info_db.txt", 'r') as file:
            for line in file:
                student_info = line.strip().split(";")
                if len(student_info) == 5:
                    _, _, _, dep, _ = student_info
                    department_counts[dep] = department_counts.get(dep, 0) + 1

        print("Number of students per department:")
        for department, count in department_counts.items():
            print(f"{department}: {count}")

    except FileNotFoundError:
        print("File not found")
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
                student_info = line.strip().split(";")
                if len(student_info) == 5:
                    stid, name, gender, dep, gpa = student_info
                    if float(gpa) > st_gpa:
                        top_students.append((name, gpa, dep))

        if top_students:
            print(f"Top scoring students with GPA greater than {st_gpa}:")
            for name, gpa, dep in top_students:
                print(f"{name} with GPA {gpa} in {dep} Department")
        else:
            print(f"No students found with GPA greater than {st_gpa}")
    except ValueError:
        print("Invalid GPA input. Please enter a numeric value.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()
# exiting program
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

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

if __name__ == "__main__":
    menu()
