import math
import time
import random
import re

# 最原始的获取素数
def isPrime1(n):
    rst = [2]
    for i in range(3, n+1):

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            rst.append(i)
    return rst


# 稍微优化的获取素数
def isPrime2(n):
    rst = [2]

    for i in range(3, n+1):

        better = int(math.sqrt(i)+2)

        for j in range(2, better):
            if i % j == 0:
                break
        else:
            rst.append(i)

    return rst


def isPrime3(l1):
    for i in range(len(l1)-1):

        for j in range(len(l1)-1-i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1

'''
l1 = list(random.randint(0, 10000) for i in range(10000))
start = time.time()
isPrime3(l1)
print(time.time()-start)

example = 'Zhejiang Normal University is an awesome Uni!'
rst = re.findall(r'\b\w+', example)
print(rst)
'''




