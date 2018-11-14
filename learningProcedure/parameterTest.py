# normal
def normal(a, b, c):
    print(a, b, c)


# default
def default(a, b, c=3):
    print(a, b, c)


# keyword
def keyword(a=1, b=2, c=3):
    print(a, b, c)


# collecting
def collecting(*args):
    # args以元组形式tuple被存储，可为空
    for index, value in args:
        print(index, '- - -', value)


def kwCollecting(**kwargs):
    # kwargs以字典形式dict被储存，可为空
    for k, v in kwargs.items():
        print(k, '- - -', v)

