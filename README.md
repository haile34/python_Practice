# python_assigment_2
# Student Management System

This is a Python program for managing student information.

## Features

- Register new students: Allows users to add new students to the database.
- Search for students by ID: Enables users to search for a specific student using their ID.
- Update student name: Allows users to modify the name of a student in the database.
- Update student GPA: Enables users to update the GPA of a student.
- Display all students: Shows a list of all registered students.
- Delete student information: Allows users to remove a student's record from the database.
- Calculate total number of students: Provides the total count of students in the database.
- Calculate total number of students based on gender: Counts the number of male and female students separately.
- Find top scoring students: Identifies the students with the highest GPA.
- Find top scoring women students: Identifies the female students with the highest GPA.
- Search for students with GPA greater than a given threshold: Allows users to find students with a GPA above a specified value.
- Display frequent student names: Shows the names of students that occur frequently in the database.
- Show number of students per department: Provides a count of students in each department.
## Usage

1. To run the program, execute the menu() function in your Python environment.
2. Make sure to have the necessary dependencies installed.
3. Follow the instructions provided by the program to perform desired operations.


### Registering a New Student

## Input Examples
Student Registration Form
1. Enter the number of students: 1
2. Enter student id: 001
3. Enter student name: John Doe
4. Enter student GPA (between 0 and 4): 3.5
5. Enter the department: Computer Science
6. Enter student gender: Male
Registered successfully.


  ## searching student
1. Enter student ID: 001
2. ____student found____
3. Name: John Doe
4. Gender: Male
5. Department: Computer Science
6. GPA: 3.5

## Updatiing student information
1. Enter student ID: 001
2. Enter corrected New Name: John Smith
3. Data of student 001 updated successfully!

## Displaying All student
 Student database:

1. ID: 001
2. Name: John Smith
3. Gender: Male
4. Department: Computer Science
5. GPA: 3.5

## Code Snippets

```python
# Register a new student
register_student()

# Search for a student
search_student()

# Update student name
update_name()

# Update student GPA
update_gpa()

# Display all students
show_all()

# Delete student information
delete_student()

# Calculate total number of students
total_students()

# Calculate total number of students based on gender
total_num_based_gen()

# Find top scoring students
top_students_per_department()

# Find top scoring women students
top_scoring_women_department()

# Search for students with GPA greater than a given threshold
above_agiven_GPA()

# Display frequent student names
used_name()

# Show number of students per department
students_per_department()
