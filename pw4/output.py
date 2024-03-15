from main import calculate_gpa

def print_sorted_students(sorted_students, course_list):
    print("Sorted student list by GPA descending:")
    for student in sorted_students:
        print(f"Student name: {student.name}, ID: {student.ID}, GPA: {calculate_gpa(student, course_list):.2f}")
