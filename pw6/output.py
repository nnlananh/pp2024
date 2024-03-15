import pickle
import os
from main import calculate_gpa
def load_students_from_file():
    if os.path.exists('students.pkl'):
        with open('students.pkl', 'rb') as file:
            return pickle.load(file)
    return []
def load_courses_from_file():
    if os.path.exists('courses.pkl'):
        with open('courses.pkl', 'rb') as file:
            return pickle.load(file)
    return []

def load_marks_from_file():
    if os.path.exists('marks.pkl'):
        with open('marks.pkl', 'rb') as file:
            return pickle.load(file)
    return []

def print_sorted_students(sorted_students, course_list):
    print("Sorted student list by GPA descending:")
    for student in sorted_students:
        print(f"Student name: {student.name}, ID: {student.ID}, GPA: {calculate_gpa(student, course_list):.2f}")
