class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lec(self, lec_name, corse, grade):
        if isinstance(lec_name, Lecturer) and corse in self.courses_in_progress and corse in lec_name.courses_attached:
            if corse in lec_name.lec_grades:
                lec_name.lec_grades[corse] += [grade]
            else:
                lec_name.lec_grades[corse] = [grade]
        else:
            return 'Ошибка'

    def aver_grade(self):
        grad = []
        for val in self.grades.values():
            grad.extend(val)
        return round(sum(grad) / len(grad), 1)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.aver_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.aver_grade() < other.aver_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): # лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}


    def aver_grade(self):
        grad = []
        for val in self.lec_grades.values():
            grad.extend(val)
        return sum(grad) / len(grad)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.aver_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.aver_grade() < other.aver_grade()

class Reviewer(Mentor): # проверяющие
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
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res

# студент №1
best_student = Student('Василий', 'Петров', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

# студент №2
best_student2 = Student('Сергей','Иванов', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Java']

# проверяющий №1
cool_mentor = Reviewer('Александра', 'Васильева')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

# проверяющий №2
cool_mentor2 = Reviewer('Елена', 'Александрова')
cool_mentor2.courses_attached += ['Python']
cool_mentor2.courses_attached += ['Java']

# лектор №1
cool_lecturer = Lecturer('Анна', 'Иванова')
cool_lecturer.courses_attached += ['Python']

# лектор №2
cool_lecturer2 = Lecturer('Валентина', 'Петрова')
cool_lecturer2.courses_attached += ['Python']

# оценки от лектора №1
cool_mentor.rate_hw(best_student, 'Python', 2)
cool_mentor.rate_hw(best_student2, 'Python', 3)
cool_mentor.rate_hw(best_student, 'Python', 4)
cool_mentor.rate_hw(best_student2, 'Python', 3)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student2, 'Python', 3)
cool_mentor.rate_hw(best_student, 'Java', 3)
cool_mentor.rate_hw(best_student2, 'Java', 3)
cool_mentor.rate_hw(best_student, 'Java', 4)
cool_mentor.rate_hw(best_student2, 'Java', 5)

# оценки от лектора №2
cool_mentor2.rate_hw(best_student, 'Python', 5)
cool_mentor2.rate_hw(best_student2, 'Python', 4)
cool_mentor2.rate_hw(best_student, 'Python', 2)
cool_mentor2.rate_hw(best_student2, 'Python', 5)
cool_mentor2.rate_hw(best_student, 'Python', 5)
cool_mentor2.rate_hw(best_student2, 'Python', 4)
cool_mentor2.rate_hw(best_student, 'Java', 5)
cool_mentor2.rate_hw(best_student2, 'Java', 3)
cool_mentor2.rate_hw(best_student, 'Java', 4)
cool_mentor2.rate_hw(best_student2, 'Java', 2)

# оценки от студента №1
best_student.rate_lec(cool_lecturer, 'Python', 5)
best_student.rate_lec(cool_lecturer2, 'Python', 6)
best_student.rate_lec(cool_lecturer, 'Java', 4)
best_student.rate_lec(cool_lecturer2, 'Java', 7)

# оценки от студента №2
best_student2.rate_lec(cool_lecturer, 'Python', 5)
best_student2.rate_lec(cool_lecturer2, 'Python', 6)
best_student2.rate_lec(cool_lecturer, 'Java', 4)
best_student2.rate_lec(cool_lecturer2, 'Java', 7)

print(best_student)
print('-----0--------')
print(best_student2)
print('------1-------')
print(cool_mentor)
print('------2-------')
print(cool_mentor2)
print('------3-------')
print(cool_lecturer)
print('-----4--------')
print(cool_lecturer2)
print('------5-------')
print(cool_lecturer > cool_lecturer2)
print(best_student > best_student2)