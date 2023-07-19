'''
Main module to control the system.
'''

from student import Student
from course import Course

student1 = Student("Pat")
student1.editPhoneNumber(123)
print(student1.phoneNumber)
student1.editEmail("hhhh@gmail.com")

student1.editPhoneNumber(222)
print(student1.phoneNumber)

