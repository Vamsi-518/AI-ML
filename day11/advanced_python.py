import logging
from functools import reduce
# LOGGING
logging.basicConfig(
    filename="advanced_python.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# STUDENT DATA
students = [
    {"id": 101, "name": "Krishna", "marks": 85},
    {"id": 102, "name": "murali", "marks": 72},
    {"id": 103, "name": "naga", "marks": 91},
    {"id": 104, "name": "Vamsi", "marks": 65}
]
# 1. ITERATOR
def iterator_example():
    print("\n========== 1. ITERATOR ==========")
    student_iterator = iter(students)
    while True:
        try:
            student = next(student_iterator)
            print(
                student["name"],
                "-",
                student["marks"]
            )
        except StopIteration:
            break
# 2. GENERATOR
def student_generator():
    for student in students:
        yield student
def generator_example():
    print("\n========== 2. GENERATOR ==========")
    for student in student_generator():
        print(
            student["name"],
            "-",
            student["marks"]
        )
# 3. DECORATOR
def logger(func):
    def wrapper():
        print("\nRunning:", func.__name__)
        logging.info(
            f"Started: {func.__name__}"
        )
        result = func()
        logging.info(
            f"Completed: {func.__name__}"
        )
        return result
    return wrapper
@logger
def show_top_students():
    print("\nTop Students:")
    for student in students:
        if student["marks"] >= 80:
            print(
                student["name"],
                "-",
                student["marks"]
            )
# 4. CONTEXT MANAGER
class ReportFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        print("\nOpening report file...")
        self.file = open(
            self.filename,
            self.mode
        )
        return self.file
    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):
        print("Closing report file...")
        if self.file:
            self.file.close()
def context_manager_example():
    print("\n========== 4. CONTEXT MANAGER ==========")
    with ReportFile(
        "student_report.txt",
        "w"
    ) as file:
        for student in students:
            file.write(
                f"{student['id']} - "
                f"{student['name']} - "
                f"{student['marks']}\n"
            )
    print("Report saved successfully.")
# 5. MAP, FILTER, REDUCE
def functional_programming():
    print("\n========== 5. MAP / FILTER / REDUCE ==========")

    marks = list(
        map(
            lambda student: student["marks"],
            students
        )
    )
    print("Marks:", marks)
    passed_students = list(
        filter(
            lambda student: student["marks"] >= 70,
            students
        )
    )
    print("\nPassed Students:")
    for student in passed_students:
        print(
            student["name"],
            "-",
            student["marks"]
        )
    total_marks = reduce(
        lambda total, mark: total + mark,
        marks,
        0
    )
    print(
        "\nTotal Marks:",
        total_marks
    )
# MAIN PROGRAM
def main():
    print("==========================================")
    print("       ADVANCED PYTHON DAY 11")
    print("==========================================")
    # 1. Iterator
    iterator_example()
# 2. Generator
    generator_example()
# 3. Decorator
    show_top_students()
# 4. Context Manager
    context_manager_example()
# 5. Map / Filter / Reduce
    functional_programming()
    print("\n==========================================")
    print("       PROGRAM COMPLETED")
    print("==========================================")
if __name__ == "__main__":
\
    main()