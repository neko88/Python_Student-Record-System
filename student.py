import problem
from constants import WarningId, ErrorId, Pronoun, Term, Course
from problem import Problem
from update import Update
from coursegrade import Grade
from courserecord import CourseRecord


PHONENUM = "phone number"
EMAIL = "email"
SET = "set"
GET = "get"
GRADE = "grade"


class Student:
    def __init__(self, name: str, birthday: str = None, pronoun: Pronoun = None):
        self.courseTerm = None
        self.name = name
        self.phoneNumber = None
        self.emailadr = None
        self.birthday = birthday
        self.pronoun = pronoun
        self.courseRecordList:CourseRecord = []

    """
     Method to SET or GET phone number.
     Classes used: Problem(), Update()
     """
    def phone_number(self, command:str=GET, number:str=None):
        val = False
        if command.lower() == SET:
            if self.phoneNumber is None:
                self.phoneNumber = number
                val = True
            else:
                val = Problem().displayWarning(WarningId.WARNING_1, PHONENUM, self.phoneNumber)
                if val is True:
                    self.phoneNumber = number
            Update().displayUpdate(val, self.name, PHONENUM, self.phoneNumber)

        elif command.lower() == GET:
            if self.phoneNumber is None:
                Problem().displayError(ErrorId.ERROR_1, PHONENUM)
            return self.phoneNumber

        else:
            Problem().displayError(ErrorId.ERROR_2, PHONENUM)


    """
    Method to SET or GET email.
    Classes used: Problem(), Update()
    """
    def email(self, command:str=GET, emailadr:str=None):
        val = False
        if command.lower() == SET:
            if self.emailadr is None:
                self.emailadr = emailadr
                val = True
            else:
                val = Problem().displayWarning(WarningId.WARNING_1, EMAIL, self.emailadr)
                if val is True:
                    self.emailadr = emailadr
            Update().displayUpdate(val, self.name, EMAIL, self.emailadr)

        elif command.lower() == GET:
            if self.emailadr is None:
                Problem().displayError(ErrorId.ERROR_1, EMAIL)
            return self.emailadr

        else:
            Problem().displayError(ErrorId.ERROR_2, EMAIL)


    def setGrade(self, course:Course, grade:Grade, term:Term, year:int):
        for rec in self.courseRecordList:
            if course == rec.course:
                if term == rec.term:
                    if year == rec.year:
                        val = Problem().displayWarning(WarningId.WARNING_1, f"{course.value} {term.value} {year}", rec.grade.value)
                        if val is True:
                            rec.grade = grade
                            return
        self.courseRecordList.append(CourseRecord(course, grade, term, year))
        Update().displayUpdate(True, self.name, f"{course.value} {term.value} {year}", grade.value)


    def getGrade(self, course:Course, term:Term, year:int):
        if self.courseRecordList is None:
            Problem().displayError(ErrorId.ERROR_2, f"{course.value} {term.value} {year}")
            return
        for rec in self.courseRecordList:
            if course == rec.course:
                if term == rec.term:
                    if year == rec.year:
                        print(f"..[Grade Record: {self.name}] {rec.course.value} {term.value} {year}: {rec.grade.value}")
                        return rec.grade.value
