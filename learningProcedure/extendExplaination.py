class A():
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('this is the private method of A.')

    def public(self):
        print('this is the public method of A.')

    def __test(self):
        print('this is the __test() of A.')


class B(A):
    def __private(self):
        print('this is the private method of B.')

    def public(self):
        print('this is the public method of B.')


class C(A):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('this is the private method of C.')

    def public(self):
        print('this is the public method of C.')


if __name__ == '__main__':
    a = A()# private A, public A
    b = B()# private A, public B
    c = C()# private C, public C