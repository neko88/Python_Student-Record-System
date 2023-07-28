
from constants import Course, Term
from coursegrade import Grade

class CourseRecord:
    def __init__add_course(self, course:Course, grade:Grade, term:Term, year:int):
        self.course = course
        self.grade = grade
        self.term = term
        self.year = year

