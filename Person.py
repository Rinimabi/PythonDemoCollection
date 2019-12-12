class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self, name):
        return self.name

    @property
    def age(self, age):
        return self.age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%splaying FlyCheese.' % self._name)
        else:
            print('%splaying ThreeKingdom.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    print(person.age)
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
