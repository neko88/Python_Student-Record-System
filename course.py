from enum import Enum

class Term(Enum):
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    FALL = "FALL"
    WINTER = "WINTER"


class Subject(Enum):
    MATH = "MATH"
    SCIENCE = "SCIENCE"
    ENGLISH = "ENGLISH"


class Course:
    def __init__(self, id:int, name:str, subject:Subject, professorName:str=None, term:Term=None):
        self.id = id
        self.courseName = name
        self.courseSubject = subject
        self.professorName = professorName
        self.term = term
        self.year = None

    def addProfessor(self, name:str):
        self.professorName = name

    def addTerm(self, term:Term, year:int):
        self.term = term
        self.year = year