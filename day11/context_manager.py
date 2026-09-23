# CONTEXT MANAGER
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        print("Opening file...")
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
        print("Closing file...")
        if self.file:
            self.file.close()
with FileManager(
    "student.txt",
    "w"
) as file:
    file.write(
        "murali - Python\n"
    )
    file.write(
        "naga - Java\n"
    )
print("\nStudent Data:")
with FileManager(
    "student.txt",
    "r"
) as file:
    data = file.read()

    print(data)