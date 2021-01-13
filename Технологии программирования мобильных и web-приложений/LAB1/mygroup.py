groupmates = [
    {
        "name": "Денис",
        "surname": "Васильев",
        "exams": ["СОС", "ИС", "ТО"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Сергей",
        "surname": "Ларионов",
        "exams": ["СОС", "ИС", "ТО"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Татьяна",
        "surname": "Никифорова",
        "exams": ["СОС", "ИС", "ТО"],
        "marks": [5, 5, 4]
    },
      {
        "name": "Владимир",
        "surname": "Пономарев",
        "exams": ["СОС", "ИС", "ТО"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Максим",
        "surname": "Фролов",
        "exams": ["СОС", "ИС", "ТО"],
        "marks": [3, 4, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)

def fun (students,avg_mark):
    stud_list=[]
    for student in students:
        marks= sum(student["marks"]) / len(student["marks"])
        if marks >= avg_mark:
            stud_list.append( student["surname"])


    return print(stud_list)

fun(groupmates,int(input("Enter average mark \n")))
