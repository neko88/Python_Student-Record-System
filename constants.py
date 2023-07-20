from enum import Enum

class Pronoun(Enum):
    HE = "HE"
    SHE = "SHE"
    NA = "N/A"

class Grade(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"

class Term(Enum):
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    FALL = "FALL"
    WINTER = "WINTER"


class Subject(Enum):
    MATH = "MATH"
    SCIENCE = "SCIENCE"
    ENGLISH = "ENGLISH"


class WarningId(Enum):
    WARNING_1 = "w001"
    WARNING_2 = "w002"
    WARNING_3 = "w003"

class ErrorId(Enum):
    ERROR_1 = "e001"
    ERROR_2 = "e002"
    ERROR_3 = "e003"