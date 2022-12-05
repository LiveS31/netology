#создание класса студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_lesson(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

        sum = 0
        len = 0

        for key in lecturer.grades.keys():
            for grad in list(lecturer.grades[key]):
                sum +=grad
                len +=1
        lecturer.average_rating = round (sum/len,1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя:{self.name}\n"\
        f"Фамилия: {self.surname}\n"\
        f"Средняя оценка за домашние задания: {self.average_rating}\n"
        f'курсы в процуссе изуцения: {", ".join(self.courses_in_progress)}\n'\
        f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res

#создание класса mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
        self.students_list = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя: {self.name}\n"\
        f"Фамилия: {self.surname}\n"\
        f"Средняя оценка за лекции: {self.average_rating}"
        return res

#создание класса Reviewer
class Reviewer(Mentor):
    def __int__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        sum =0
        len =0

        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum  += grad
                len += 1
        student.average_rating = round(sum / len, 1)
    def __str__(self):
        res = f"Имя: {self.name}\n"\
            f"Фамилия: {self.surname}"
        return res

###
def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator +=1
    return round(sum_course_grade / iterator)
###
def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade/iterator)


#####
first_student = Student("Иван", "Пивнов", "м")
first_student.finished_courses += ["Java"]
first_student.courses_in_progress += ["GIT"]
first_student.courses_in_progress += ["Python"]
######
second_student = Student("Емеля", "Печкин", "м")
second_student.courses_in_progress += ["Python"]
second_student.finished_courses += ["C#"]
######
first_lecturer = Lecturer("Василий", "Сказочников")
first_lecturer.courses_attached += ["Python"]
first_lecturer.courses_attached += ["GIT"]
######
second_lecturer = Lecturer("Руслан", "Людмилин")
second_lecturer.courses_attached += ["GIT"]
#####
first_reviewer = Reviewer("Руслан", "Ромин")
first_reviewer.courses_attached += ["Python"]
######
second_reviewer = Reviewer("Александр", "Светлаков")
second_reviewer.courses_attached += ["GIT"]
second_reviewer.courses_attached += ["Python"]
######

student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

####

first_student.rate_lesson(second_lecturer, "GIT", 9)
first_student.rate_lesson(second_lecturer, "GIT", 10)
first_student.rate_lesson(first_lecturer, "GIT", 9)
first_student.rate_lesson(first_lecturer, "GIT", 9)
first_student.rate_lesson(first_lecturer, "Python", 9)
second_student.rate_lesson(first_lecturer, "Python", 10)
second_student.rate_lesson(first_lecturer, "Python", 10)

second_reviewer.rate_hw(first_student, "Python", 10)
second_reviewer.rate_hw(first_student, "GIT", 9)
second_reviewer.rate_hw(first_student, "GIT", 10)
first_reviewer.rate_hw(first_student, "Python", 10)
first_reviewer.rate_hw(second_student, "Python", 9)
first_reviewer.rate_hw(second_student, "Python", 9)
first_reviewer.rate_hw(second_student, "Python", 9)

print("Список лекторов:")
print(f"{first_lecturer}\n")
print(f"{second_lecturer}\n")
print("Список проверяющих:")
print(f"{first_reviewer}\n")
print(f"{second_reviewer}\n")
print("Список студентов:")
print(f"{first_student}\n")
print(f"{second_student}\n")

##
if  (first_student > second_student) == True:
    answer_student = 'Верно'
else:
    answer_student = 'Неврно'

if (second_lecturer < first_lecturer) == True:
    answer_lecturer = "Верно"
else:
    answer_lecturer = 'Неверно'
##
print(f"Средняя оценка за дз у {first_student.surname}а больше, чем у {second_student.surname}а - {answer_student}")
print(f"Средняя оценка за лекции у {second_lecturer.surname}а меньше, чем у {first_lecturer.surname}а "
      f"- {answer_lecturer}\n")

print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lesson(lecturer_list, "GIT")}')
