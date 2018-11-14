# 乘法表
def mul(n):
    for line in range(1, n+1):

        for row in range(1, line+1):
            rst = row * line
            print(rst, end=' ')

        print()


# 斐波那契数列 fib
def fib(n):
    a, b = 1, 1

    for i in range(2, n+1):
        a, b = b, a+b

    return a




