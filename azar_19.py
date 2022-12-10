class Human:
    name = ''
    family = ''
    age = 0

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def speak(self):
        print('speak')

    def move(self):
        print("move")


class Student(Human):
    grade = ''

    def go_to_school(self):
        print('go to school')


s1 = Student('nikan', 'rezaei', 33)
print(s1.name)
s1.speak()
s1.grade = "A"
s1.go_to_school()
