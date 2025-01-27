#Write a function that takes a dictionary with information about students. Return info
#about the youngest student
#Find student with highest average score




def find_youngest_student(students_info):
    highest_age = 0
    for student_id, student_information in students_info.items():
        if student_information['age'] > highest_age:
            highest_age = student_information['age']
            youngest_student = student_information

    return  youngest_student



students_info = {
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'subjects': ['Math', 'Physics', 'English'],
        'scores': [7, 9, 9, 6],
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 19,
        'subjects': ['Chemistry', 'Biology', 'History'],
        'scores': [5, 6, 8, 10],
    },
    'student3': {
        'name': 'Bob Johnson',
        'age': 21,
        'subjects': ['Computer Science', 'Statistics', 'Psychology'],
        'scores': [8, 8, 9, 9, 9],
    },
}


print(find_youngest_student(students_info))
