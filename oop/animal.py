import abc


class Animal(metaclass=abc.ABCMeta):
    '''
    抽象类，拥有抽象方法category()
    '''
    def __init__(self, name='HelloWorld', age=0, gender='Unknown'):
        self.setName(name)
        self.setAge(age)
        self.setGender(gender)

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self, gender):
        self._gender = gender

    def getGender(self):
        return self._gender

    # 抽象方法
    @abc.abstractmethod
    def category(self):
        pass


class Dog(Animal):
    def __init__(self, name='Poppy', age=1, gender='female', category='dog'):
        super(Dog, self).__init__(name, age, gender)
        self.setCategory(category)

    def setCategory(self, category):
        self._category = category

    def getCategory(self):
        return self._category

    # 实现父类的抽象方法
    def category(self):
        print('Hello, I am a {0}. My name is {1}.'.format(self.getCategory(), self.getName()))


if __name__ == '__main__':
    poppy = Dog()
    poppy.category()
