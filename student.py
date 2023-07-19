from enum import Enum

import student
from warning import Warning
from update import Update
from enum import Enum


class Pronoun(Enum):
    HE = "HE"
    SHE = "SHE"
    NA = "N/A"


warning = Warning()
update = Update()


class Student:
    def __init__(self, name: str, birthday: str = None, pronoun: Pronoun = None):
        self.courseTerm = None
        self.name = name
        self.phoneNumber = None
        self.email = None
        self.birthday = birthday
        self.pronoun = pronoun
        self.courseHistory = None

    def editPhoneNumber(self, phoneNumber:int):
        PHONENUM = "phone number"
        val = False

        if self.phoneNumber is None:
            self.phoneNumber = phoneNumber
            val = True

        else:
            val = warning.displayWarning("w001", PHONENUM)
            if val is True:
                self.phoneNumber = phoneNumber
                val = True
            else:
                val = False

        update.displayUpdate(val, self.name, PHONENUM, self.phoneNumber)

    def editEmail(self, email):
        if self.email is not None:
            val = warning.displayWarning("w001", "email")
            if val == 1:
                return
        self.email = email

    def course(self, courseTerm):
        self.courseHistory = []
        self.courseTerm = courseTerm
