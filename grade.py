from course import Term
from course import Subject
from enum import Enum

class Grade(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"

class Grade:
    def __init__(course, term:Term, year, grade:Grade):
        course.grade = grade
        course.term = term
        course.year = year
