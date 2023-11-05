class Student:
    """Шаблон класса Student"""
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade_lecturer:
                lecturer.grade_lecturer[course] += [grade]
            else:
                lecturer.grade_lecturer[course] = [grade]
        else:
            return 'Ошибка'


    def average_point_student(self):
        total_score = 0
        for sum_score in self.grades.values():
            sum_grade = 0
            for grade in sum_score:
                sum_grade += grade
                score_midl = sum_grade / len(sum_score)
            total_score += score_midl
        if total_score == 0:
            return f'Оценок нет!'
        else:
            return round(total_score / len(self.grades.values()), 2)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_point_student() == other.average_point_student()
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_point_student() < other.average_point_student()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_point_student() > other.average_point_student()
        else:
            return 'Ошибка'


    def __str__(self):
        self.courses_in_progress = ", ".join(self.courses_in_progress)
        self.finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_point_student()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: {self.finished_courses}")


class Mentor:
    """Шаблон класса Mentor - родительский"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Шаблон класса Lecturer, наследуемый от Mentor"""
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lecturer = {}
        Lecturer.lecturer_list.append(self)


    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_point_Lecturer() == other.average_point_Lecturer()
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_point_Lecturer() < other.average_point_Lecturer()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_point_Lecturer() > other.average_point_Lecturer()
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_point_Lecturer()}")


    def average_point_Lecturer(self):
        total_score = 0
        for sum_score in self.grade_lecturer.values():
            sum_grade = 0
            for grade in sum_score:
                sum_grade += grade
                score_midl = sum_grade / len(sum_score)
            total_score += score_midl
        if total_score == 0:
            return f'Оценок нет!'
        else:
            return round(total_score / len(self.grade_lecturer.values()), 2)

class Reviewer(Mentor):
    """Шаблон класса Reviewer, наследуемый от Mentor"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")



print('Студенты:')
student_1 = Student("Jan", "Makarsky", "Man")
student_1.courses_in_progress = ["Python", "Git"]
student_1.finished_courses = ["Введение в программирование"]

reviewer = Reviewer("Some", "Buddy")
reviewer.courses_attached = ["Python", "Git"]

reviewer.rate_hw(student_1, "Python", 10)
reviewer.rate_hw(student_1, "Python", 8)
reviewer.rate_hw(student_1, "Git", 10)
reviewer.rate_hw(student_1, "Git", 7)

student_2 = Student("Irina", "Vantseva", "Femail")
student_2.courses_in_progress = ["Python", "Git"]
student_2.finished_courses = ["Введение в программирование"]

reviewer = Reviewer("Vasiliy", "Vasiliev")
reviewer.courses_attached = ["Python", "Git"]
reviewer_1 = Reviewer("Ignat", "Ignatiev")
reviewer_1.courses_attached = ["Python", "Git"]

reviewer.rate_hw(student_2, "Python", 4)
reviewer.rate_hw(student_2, "Python", 6)
reviewer.rate_hw(student_2, "Git", 8)
reviewer.rate_hw(student_2, "Git", 10)

print(student_1, student_2, sep = '\n')
print(student_1 == student_2)
print(student_1 < student_2)
print(student_1 > student_2)
print()

print('Лекторы:')
lecturer_1 = Lecturer("Viktor", "Svetlov")
lecturer_1.courses_attached += ['Python', 'Git']

student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Git', 7)

lecturer_2 = Lecturer("Aleksandr", "Ignatiev")
lecturer_2.courses_attached += ['Python', 'Git']

student_2.rate_lecturer(lecturer_2, 'Git', 8)
student_1.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 9)

print(lecturer_1, lecturer_2, sep='\n')
print(lecturer_1 == lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print()
print('Проверяющие:')
print(reviewer, reviewer_1, sep = '\n')
print()


def student_rate_course(student_list, course_name):
    for student in student_list:
        for keys, rate in student.grades.items():
            if course_name == keys:
                sum_average = sum(rate) / len(rate)
                print(f"У студента {student.name} {student.surname} на курсе {course_name} средний бал {round(sum_average, 2)}")

def lecturer_rate_course(lecturer_list, course_name):
    for lecturer in lecturer_list:
        for keys, rate in lecturer.grade_lecturer.items():
            if course_name == keys:
                sum_average = sum(rate) / len(rate)
                print(f"У лектора {lecturer.name} {lecturer.surname} на курсе {course_name} средний бал {round(sum_average, 2)}")

student_rate_course(Student.student_list, "Git")
lecturer_rate_course(Lecturer.lecturer_list, "Git")