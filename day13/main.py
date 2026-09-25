from api_client import get_students, get_student
from student import Student
def main():
    print("DAY 13 - REST API PROJECT")
    print("\n========== ALL STUDENTS ==========")
    students = get_students()
    for data in students:

        student = Student(
            data["id"],
            data["name"],
            data["email"]
        )
        student.display()
    print("\n========== SINGLE STUDENT ==========")
    data = get_student(1)
    if data:
        student = Student(
            data["id"],
            data["name"],
            data["email"]
        )
        student.display()
    print("==========PROGRAM COMPLETED==========")
if __name__ == "__main__":
    main()