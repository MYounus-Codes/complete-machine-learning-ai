"""Advanced OOP project: model a small school system."""


class Person:
    """Shared base class for people in the school."""

    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        """Return a short description."""

        return self.name


class Student(Person):
    """Student who can enroll in classes."""

    def __init__(self, name: str, grade: int) -> None:
        super().__init__(name)
        self.grade = grade
        self.courses: list[str] = []

    def enroll(self, course: str) -> None:
        self.courses.append(course)

    def describe(self) -> str:
        return f"Student {self.name} in grade {self.grade}"


class Teacher(Person):
    """Teacher who teaches a subject."""

    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def describe(self) -> str:
        return f"Teacher {self.name} teaches {self.subject}"


class School:
    """Store students and teachers together."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def add_teacher(self, teacher: Teacher) -> None:
        self.teachers.append(teacher)

    def roster(self) -> list[str]:
        """Return descriptions for every person."""

        people = [person.describe() for person in self.students]
        people.extend(teacher.describe() for teacher in self.teachers)
        return people


def main() -> None:
    """Run the advanced project."""

    school = School("Complete ML AI School")

    student_one = Student("Amina", 10)
    student_one.enroll("Python")

    student_two = Student("Zoya", 9)
    student_two.enroll("Data Types")

    teacher = Teacher("Mr. Khan", "Programming")

    school.add_student(student_one)
    school.add_student(student_two)
    school.add_teacher(teacher)

    for line in school.roster():
        print(line)


if __name__ == "__main__":
    main()