from constants import Grade, Term

class CourseGrade:
    def __init__(course, term:Term, year, grade:Grade):
        course.grade = grade
        course.term = term
        course.year = year