"""Object-oriented programming examples for beginners."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Student:
    """Represent a student and the actions they can perform."""

    school_name = "Complete Machine Learning AI Academy"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self._progress = 0

    def introduce(self) -> str:
        """Return a short introduction."""

        return f"My name is {self.name} and I am {self.age} years old."

    def study(self, hours: int) -> None:
        """Increase progress after studying."""

        self._progress += hours

    @property
    def progress(self) -> int:
        """Expose progress as a read-only property."""

        return self._progress

    @classmethod
    def school(cls) -> str:
        """Return the school name."""

        return cls.school_name

    @staticmethod
    def is_adult(age: int) -> bool:
        """Return True for adult ages."""

        return age >= 18


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self) -> str:
        """Return the sound made by the animal."""


class Dog(Animal):
    """Concrete animal implementation."""

    def sound(self) -> str:
        return "Woof"


class Cat(Animal):
    """Another concrete animal implementation."""

    def sound(self) -> str:
        return "Meow"


def speak(animal: Animal) -> str:
    """Demonstrate polymorphism."""

    return animal.sound()


if __name__ == "__main__":
    student = Student("Amina", 21)
    student.study(3)

    print(student.introduce())
    print("School:", Student.school())
    print("Adult:", Student.is_adult(student.age))
    print("Progress:", student.progress)
    print("Dog sound:", speak(Dog()))
    print("Cat sound:", speak(Cat()))