import json
import logging
# LOGGING
logging.basicConfig(
    filename="student_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# CUSTOM EXCEPTIONS
class StudentError(Exception):
    pass
class AgeError(StudentError):
    pass
class StudentNotFoundError(StudentError):
    pass
# CONTEXT MANAGER
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
# STUDENT CLASS
class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    def __str__(self):
        return (
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Course: {self.course}"
        )

# STUDENT MANAGER
class StudentManager:
    JSON_FILE = "students.json"
    def __init__(self):
        self.students = []
        self.load_students()

# LOAD STUDENTS
    def load_students(self):
        try:
            with FileManager(self.JSON_FILE, "r") as file:
                data = json.load(file)
                for student in data:
                    self.students.append(
                        Student(
                            student["id"],
                            student["name"],
                            student["age"],
                            student["course"]
                        )
                    )
            logging.info("Students loaded successfully.")
        except FileNotFoundError:
            logging.warning(
                "students.json not found."
            )
        except json.JSONDecodeError:
            logging.error(
                "Invalid JSON file."
            )
# SAVE STUDENTS

    def save_students(self):
        data = []
        for student in self.students:
            data.append(student.to_dict())
        with FileManager(self.JSON_FILE, "w") as file:
            json.dump(
                data,
                file,
                indent=4
            )
        logging.info("Students saved successfully.")
# ADD STUDENT

    def add_student(
        self,
        student_id,
        name,
        age,
        course
    ):
        if age < 18:
            raise AgeError(
                "Age must be 18 or above."
            )
        for student in self.students:
            if student.student_id == student_id:
                raise StudentError(
                    "Student ID already exists."
                )
        student = Student(
            student_id,
            name,
            age,
            course
        )
        self.students.append(student)
        self.save_students()
        logging.info(
            f"Student added: {student_id}"
        )    
# VIEW STUDENTS
    def view_students(self):
        if not self.students:
            print("\nNo students found.")
            return
        print("\n========== STUDENTS ==========")
        for student in self.students:
            print(student)
# SEARCH STUDENT
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found:")
                print(student)
                return
        raise StudentNotFoundError(
            "Student not found."
        )
# UPDATE STUDENT
    def update_student(
        self,
        student_id,
        name,
        age,
        course
    ):
        if age < 18:
            raise AgeError(
                "Age must be 18 or above."
            )
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.age = age
                student.course = course
                self.save_students()
                logging.info(
                    f"Student updated: {student_id}"
                )
                print(
                    "\nStudent updated successfully."
                )
                return
        raise StudentNotFoundError(
            "Student not found."
        )
# DELETE STUDENT
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                logging.info(
                    f"Student deleted: {student_id}"
                )
                print(
                    "\nStudent deleted successfully."
                )
                return
        raise StudentNotFoundError(
            "Student not found."
        )
# MAIN PROGRAM
def main():
    manager = StudentManager()
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        try:
# ADD
            if choice == "1":
                student_id = input(
                    "Enter Student ID: "
                )
                name = input(
                    "Enter Name: "
                )
                age = int(
                    input("Enter Age: ")
                )
                course = input(
                    "Enter Course: "
                )
                manager.add_student(
                    student_id,
                    name,
                    age,
                    course
                )
                print(
                    "\nStudent added successfully."
                )
# VIEW
            elif choice == "2":
                manager.view_students()
# SEARCH
            elif choice == "3":
                student_id = input(
                    "Enter Student ID: "
                )
                manager.search_student(
                    student_id
                )

# UPDATE
            elif choice == "4":
                student_id = input(
                    "Enter Student ID: "
                )
                name = input(
                    "Enter New Name: "
                )
                age = int(
                    input("Enter New Age: ")
                )
                course = input(
                    "Enter New Course: "
                )
                manager.update_student(
                    student_id,
                    name,
                    age,
                    course
                )
# DELETE
            elif choice == "5":
                student_id = input(
                    "Enter Student ID: "
                )
                manager.delete_student(
                    student_id
                )
# EXIT
            elif choice == "6":
                print(
                    "\nThank you for using Student Management System!"
                )
                break
            else:
                print(
                    "\nInvalid choice."
                )
        except ValueError:
            print(
                "\nPlease enter a valid number."
            )
            logging.error(
                "Invalid number entered."
            )
        except AgeError as e:
            print(
                f"\nError: {e}"
            )
            logging.error(str(e))
        except StudentNotFoundError as e:
            print(
                f"\nError: {e}"
            )
            logging.error(str(e))
        except StudentError as e:
            print(
                f"\nError: {e}"
            )
            logging.error(str(e))
        except Exception as e:
            print(
                f"\nUnexpected error: {e}"
            )
            logging.exception(
                "Unexpected error occurred."
            )
# START PROGRAM
if __name__ == "__main__":
    main()