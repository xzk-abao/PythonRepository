
from re import S


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def  study(self, course_name):
        print(f'学生正在学习{course_name}')

    def play(self):
        print(f'学生正在玩游戏.')

stu1 = Student('L', 23)
stu2 = Student('A', 232)

print(stu1)
print(stu2)
print(hex(id(stu1)), hex(id(stu2)))