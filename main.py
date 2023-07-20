'''
Main module to control the system.
'''

from student import Student
from course import Course

SET = "set"
GET = "get"

student1 = Student("Pat")
student1.phone_number(SET, "99-0392")
student1.email("hhhh@gmail.com")

student1.phone_number(SET, "222")

#
