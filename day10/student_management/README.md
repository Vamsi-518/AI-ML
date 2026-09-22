I’ll trace the student management project from its README into the Python code and data file, then explain the full flow in beginner-friendly steps with the relevant file links.

Read 

Read 

Read 

Your **Student Management System** is a command-line Python application. It stores student data in a JSON file and supports adding, viewing, searching, updating, and deleting students.

Files:

- `student_management.py`: Main Python program
- `students.json`: Student data storage
- `README.md`: Currently empty

## 1. Run the program

Open PowerShell in the project folder:

```powershell
cd E:\AI_ML\day10\student_management
python student_management.py
```

The program starts from this section:

```python
if __name__ == "__main__":
    main()
```

This calls the `main()` function.

## 2. Import modules

```python
import json
import logging
```

`json` is used to read and write `students.json`.

`logging` records program events such as:

- Students loaded
- Students added
- Students updated
- Students deleted
- Errors

A log file named `student_management.log` is created automatically.

## 3. Custom exceptions

```python
class StudentError(Exception):
    pass

class AgeError(StudentError):
    pass

class StudentNotFoundError(StudentError):
    pass
```

These are custom error types.

### `StudentError`

Used for general student-related errors, such as duplicate IDs.

### `AgeError`

Used when the student's age is below 18.

```python
if age < 18:
    raise AgeError("Age must be 18 or above.")
```

### `StudentNotFoundError`

Used when searching, updating, or deleting a student that does not exist.

## 4. FileManager context manager

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
```

This class manages opening and closing files.

### Opening the file

```python
def __enter__(self):
    self.file = open(self.filename, self.mode)
    return self.file
```

### Closing the file

```python
def __exit__(self, exc_type, exc_value, traceback):
    if self.file:
        self.file.close()
```

It is used like this:

```python
with FileManager("students.json", "r") as file:
    data = json.load(file)
```

The file is automatically closed after the `with` block finishes.

## 5. Student class

```python
class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
```

This class represents one student.

For example:

```python
student = Student("05", "Ravi", 21, "CSE")
```

The object contains:

```text
ID: 05
Name: Ravi
Age: 21
Course: CSE
```

### Convert a student to a dictionary

```python
def to_dict(self):
    return {
        "id": self.student_id,
        "name": self.name,
        "age": self.age,
        "course": self.course
    }
```

JSON cannot directly store a Python object, so `to_dict()` converts the object into a dictionary.

### Display a student

```python
def __str__(self):
    return (
        f"ID: {self.student_id} | "
        f"Name: {self.name} | "
        f"Age: {self.age} | "
        f"Course: {self.course}"
    )
```

This controls how the student appears when printed.

## 6. StudentManager class

```python
class StudentManager:
    JSON_FILE = "students.json"
```

This class contains all student operations.

It stores students in a list:

```python
self.students = []
```

When the manager is created:

```python
manager = StudentManager()
```

Python automatically calls:

```python
def __init__(self):
    self.students = []
    self.load_students()
```

So existing students are loaded immediately from `students.json`.

## 7. Loading students

```python
def load_students(self):
```

The method opens the JSON file:

```python
with FileManager(self.JSON_FILE, "r") as file:
    data = json.load(file)
```

The JSON data looks like this:

```json
{
    "id": "01",
    "name": "vamsi",
    "age": 19,
    "course": "cse"
}
```

Each dictionary is converted into a `Student` object:

```python
self.students.append(
    Student(
        student["id"],
        student["name"],
        student["age"],
        student["course"]
    )
)
```

If the file does not exist:

```python
except FileNotFoundError:
```

the program logs a warning instead of crashing.

If the JSON is invalid:

```python
except json.JSONDecodeError:
```

the program logs an error.

## 8. Saving students

```python
def save_students(self):
```

First, every `Student` object is converted into a dictionary:

```python
data = []

for student in self.students:
    data.append(student.to_dict())
```

Then the list is written back to the JSON file:

```python
with FileManager(self.JSON_FILE, "w") as file:
    json.dump(data, file, indent=4)
```

The `indent=4` makes the JSON file readable.

Saving happens after:

- Adding a student
- Updating a student
- Deleting a student

## 9. Adding a student

When the user selects option `1`, the program asks for:

```text
Student ID
Name
Age
Course
```

The age is converted from text to an integer:

```python
age = int(input("Enter Age: "))
```

Then this method is called:

```python
manager.add_student(student_id, name, age, course)
```

Inside `add_student()`:

### Age validation

```python
if age < 18:
    raise AgeError("Age must be 18 or above.")
```

### Duplicate ID validation

```python
for student in self.students:
    if student.student_id == student_id:
        raise StudentError("Student ID already exists.")
```

### Create and store the student

```python
student = Student(student_id, name, age, course)
self.students.append(student)
```

### Save the updated list

```python
self.save_students()
```

Example:

```text
Enter Student ID: 05
Enter Name: Ravi
Enter Age: 21
Enter Course: Python
```

The new record is added to `students.json`.

## 10. Viewing all students

When the user selects option `2`:

```python
manager.view_students()
```

The method checks whether the list is empty:

```python
if not self.students:
    print("\nNo students found.")
    return
```

Otherwise, it prints each student:

```python
for student in self.students:
    print(student)
```

Because the `Student` class has a `__str__()` method, each student displays in a readable format.

## 11. Searching for a student

When the user selects option `3`, they enter a student ID.

```python
manager.search_student(student_id)
```

The method checks every student:

```python
for student in self.students:
    if student.student_id == student_id:
        print(student)
        return
```

If no matching ID is found:

```python
raise StudentNotFoundError("Student not found.")
```

## 12. Updating a student

When the user selects option `4`, the program asks for:

```text
Student ID
New Name
New Age
New Course
```

Then it calls:

```python
manager.update_student(
    student_id,
    name,
    age,
    course
)
```

The method finds the student and replaces the old values:

```python
student.name = name
student.age = age
student.course = course
```

Then it saves the updated data:

```python
self.save_students()
```

The student ID is not changed.

## 13. Deleting a student

When the user selects option `5`, the user enters an ID:

```python
manager.delete_student(student_id)
```

The matching object is removed from the list:

```python
self.students.remove(student)
```

Then the updated list is saved to the JSON file.

## 14. Main menu loop

The menu is inside:

```python
while True:
```

This means the menu keeps appearing until the user chooses option `6`.

The options are:

```text
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

When option `6` is selected:

```python
break
```

The loop stops and the program ends.

## 15. Error handling

The program uses `try` and `except`:

```python
try:
    # menu operations
except ValueError:
    ...
except AgeError as e:
    ...
except StudentNotFoundError as e:
    ...
except StudentError as e:
    ...
except Exception as e:
    ...
```

### Invalid number

If the user enters text instead of an age:

```text
Enter Age: twenty
```

`int()` raises `ValueError`.

The program displays:

```text
Please enter a valid number.
```

### Invalid age

If the user enters `17`:

```text
Error: Age must be 18 or above.
```

### Missing student

If the user searches for ID `99`:

```text
Error: Student not found.
```

### Duplicate ID

If the user adds an existing ID:

```text
Error: Student ID already exists.
```

## 16. Complete program flow

The complete flow is:

```text
Program starts
     |
Create StudentManager
     |
Load students.json
     |
Display menu
     |
User selects an option
     |
Perform add/view/search/update/delete
     |
Save changes to students.json
     |
Display menu again
     |
User selects Exit
     |
Program ends
```

One important detail: run the command from the `student_management` folder because the program uses the relative filename `students.json`.s