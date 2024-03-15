import math
from domains.student import Student
from domains.course import Course
from input import *
from output import *

def floor_mark(mark):
    return math.floor(mark * 10) / 10

def calculate_gpa(student, course_list):
    weighted_sum = 0
    total_credits = 0
    for mark, course in zip(student.marks, course_list):
        weighted_sum += mark * course.credits
        total_credits += course.credits
    return weighted_sum / total_credits

def sort_students_by_gpa(student_list, course_list):
    student_gpa = [(student, calculate_gpa(student, course_list)) for student in student_list]
    sorted_students = sorted(student_gpa, key=lambda x: x[1], reverse=True)
    return [student[0] for student in sorted_students]

def main():
    student_list = []
    nb_student = input_number_of_students()
    for i in range(nb_student):
        student_id, student_name, student_dob = input_student_details(i)
        student_list.append(Student(student_id, student_name, student_dob))
        
    course_list = []
    nb_course = input_number_of_courses()
    for j in range(nb_course):
        course_id, course_name, course_credits = input_course_details(j)
        course_list.append(Course(course_id, course_name, course_credits))
        
    for student in student_list:
        for course in course_list:
            mark = input_mark(course.name, student.name)
            student.add_mark(floor_mark(mark))
    
    sorted_students = sort_students_by_gpa(student_list, course_list)

    print_sorted_students(sorted_students, course_list)

if __name__ == "__main__":
    main()
