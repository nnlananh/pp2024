# input.py

def input_number_of_students():
    return int(input("Input number of students: "))

def input_student_details(i):
    student_id = input(f"Input ID of student {i+1}: ")
    student_name = input(f"Input name of student {i+1}: ")
    student_dob = input(f"Input the birth date of student {i+1}: ")
    
    # Write student data to students.txt
    with open('C:\\Users\\lanan\\pp2024\\pw5\\students.txt', 'a') as file:
        file.write(f"{student_id},{student_name},{student_dob}\n")

    return student_id, student_name, student_dob

def input_number_of_courses():
    return int(input("Input number of courses: "))

# input.py

def input_course_details(j):
    course_id = input(f"Input ID of course {j+1}: ")
    course_name = input(f"Input name of course {j+1}: ")
    course_credits = float(input(f"Input number of credits for course {j+1}: "))
    
    # Write course data to courses.txt
    with open('C:\\Users\\lanan\\pp2024\\pw5\\courses.txt', 'a') as file:
        file.write(f"{course_id},{course_name},{course_credits}\n")

    return course_id, course_name, course_credits


def input_mark(course_name, student_name):
    mark = float(input(f"Input mark of {course_name} for student {student_name}: "))
    
    # Write mark data to marks.txt
    with open('C:\\Users\\lanan\\pp2024\\pw5\\marks.txt', 'a') as file:
        file.write(f"{student_name},{course_name},{mark}\n")

    return mark
