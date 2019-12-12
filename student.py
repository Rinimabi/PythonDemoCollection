class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def test(self):
        print('asdasda')


stu1 = Student('Chris', 38)
stu1.study('Python程序设计')
stu1.test()


class Test:
    def __init__(self, foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print('__bar')

test = Test('hello')
# test.__bar()
# print(test.__foo)

