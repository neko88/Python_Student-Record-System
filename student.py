from enum import Enum

class Pronoun(Enum):
    HE = "HE"
    SHE = "SHE"
    NA = "N/A"

class Student:
    def __init__(student, name:str, birthday:str=None, pronoun:Pronoun=None):
        student.courseTerm = None
        student.name = name
        student.birthday = birthday
        student.pronoun = pronoun
        student.courseHistory = None

    def addPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def addEmail(self,email):
        self.email = email

    def newCourseHistory(self, courseTerm):
        self.courseHistory = []
        self.courseTerm = courseTerm
        
        