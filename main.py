'''
Main module to control the system.
'''

from student import Student
from constants import Course, Term, Grade

SET = "set"
GET = "get"

student1 = Student("Pat")
student1.phone_number(SET, "99-0392")
print(student1.email(GET))
student1.email(SET, "hhhh@gmail.com")
student1.email(GET)

student1.phone_number(SET, "222")

student1.email(GET)

student1.setGrade(Course.MATH, Grade.A, Term.FALL, 2023)
student1.setGrade(Course.MATH, Grade.B, Term.FALL, 2023)
student1.getGrade(Course.MATH, Term.FALL, 2023)
