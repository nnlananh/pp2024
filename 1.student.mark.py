nb=int(input("Input number of student in class"))
idStudent_list=[]
nameStudent_list=[]
idCourse_list=[]
nameCourse_list=[]
mark_list=[]
for i in range(nb):
    print(f"Input information of student {i+1}:")
    id_student= input(f"Input the ID of student{i+1}:")
    idStudent_list.append(id_student)
    name_student=input(f"Input the name of student{i+1}:")
    nameStudent_list.append(name_student)
    print(f"Input the number of course of student {i+1}:")
    course=int(input(f"Input the number of course for student{i+1}:"))
    for j in range(course):
        id_course=input(f"Input id of course {j+1}:")
        idCourse_list.append(id_course)
        name_course=input(f"Input name of course {j+1}:")
        nameCourse_list.append(name_course)
for a in range(len(nameCourse_list)):
    course=input("Select a course by type the ID:")
    for b in range(len(nameStudent_list)):
        mark=input(f"Input mark for student {b+1}")
        mark_list[b]=[]
        mark_list[b].a 
        
        
        
        
    
