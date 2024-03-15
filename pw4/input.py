def input_number_of_students():
    return int(input("Input number of students: "))

def input_student_details(i):
    student_id = input(f"Input ID of student {i+1}: ")
    student_name = input(f"Input name of student {i+1}: ")
    student_dob = input(f"Input the birth date of student {i+1}: ")
    return student_id, student_name, student_dob

def input_number_of_courses():
    return int(input("Input number of courses: "))

def input_course_details(j):
    course_id = input(f"Input ID of course {j+1}: ")
    course_name = input(f"Input name of course {j+1}: ")
    course_credits = float(input(f"Input number of credits for course {j+1}: "))
    return course_id, course_name, course_credits

def input_mark(course_name, student_name):
    return float(input(f"Input mark of {course_name} for student {student_name}: "))
