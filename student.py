import problem
from constants import WarningId, ErrorId, Pronoun
from problem import Problem
from update import Update


PHONENUM = "phone number"
EMAIL = "email"
SET = "set"
GET = "get"


class Student:
    def __init__(self, name: str, birthday: str = None, pronoun: Pronoun = None):
        self.courseTerm = None
        self.name = name
        self.phoneNumber = None
        self.emailadr = None
        self.birthday = birthday
        self.pronoun = pronoun
        self.courseHistory = None

    """
    Method to add phone number.
    Warning and update messages depending on return for bool in val.
    """
    def phone_number(self, command:str=GET, number:str=None):
        val = False
        if command.lower() == SET:
            if self.phoneNumber is None:
                self.phoneNumber = number
                val = True
            else:
                val = Problem().displayWarning(WarningId.WARNING_1, PHONENUM)
                if val is True:
                    self.phoneNumber = number
            Update().displayUpdate(val, self.name, PHONENUM, self.phoneNumber)

        elif command.lower() == GET:
            if self.phoneNumber is None:
                Problem().displayError(ErrorId.ERROR_1, PHONENUM)
            return self.phoneNumber


    """
    Method to add email.
    Warning and update messages depending on return for bool in val.
    """
    def email(self, command:str=GET, emailadr:str=None):
        val = False
        if command.lower() == SET:
            if self.emailadr is None:
                self.emailadr = emailadr
                val = True
            else:
                val = Problem.displayWarning(WarningId.WARNING_1, EMAIL)
                if val is True:
                    self.emailadr = emailadr
            Update.displayUpdate(val, self.name, EMAIL, self.emailadr)

        elif command.lower() == GET:
            return self.emailadr



    def course(self, courseTerm):
        self.courseHistory = []
        self.courseTerm = courseTerm
