import math
import re
import time
import string
import random
from datetime import datetime as dt
import os


class Algorithm(object):
    def __init__(self):
        pass

    # 打印乘法表
    def mul(self, n):
        for line in range(1, n + 1):

            for row in range(1, line + 1):
                rst = row * line
                print(rst, end=' ')

    # 斐波那契数列 fib
    def fib(self, n):
        a, b = 1, 1

        for i in range(2, n + 1):
            a, b = b, a + b

        return a

    # 大小写转换
    def convertToLower(self, content):
        '''
        该方法把字符串中的大写字母变成小写字母，小写字母变成大写字母。
        其实python自带的swapcase()有这个功能
        例如：axDsVaLmFnjNzk => AXdSvAlMfNJnZK
        :param content: 输入的字符串内容 axDsVaLmFnjNzk
        :return: 转换后的内容 AXdSvAlMfNJnZK
        '''
        rst1 = []

        for i in content:
            if 'A' <= i <= 'Z':
                small = i.lower()
                rst1.append(small)
            elif 'a' <= i <= 'z':
                large = i.upper()
                rst1.append(large)
            else:
                rst1.append(i)

        rst2 = ''.join(rst1)
        return rst2

    # 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for k, v in enumerate(nums):
            rst = target - v
            if rst not in d:
                d[v] = k
            else:
                return [d[rst], k]

    # 文字过滤器
    def textFilter(self, text):
        limitedText = ['操', '日', '尼玛', '鸡', '草']
        for i in limitedText:
            if i in text:
                text = text.replace(i, '***')
        return text

    def isPrime(self, n):
        rst = [2]

        for i in range(3, n + 1):

            better = int(math.sqrt(i) + 2)

            for j in range(2, better):
                if i % j == 0:
                    break
            else:
                rst.append(i)

        return rst


if __name__ == '__main__':
    test = Algorithm()

    '''
    content = input('请输入字符串：')
    result = test.convertToLower(content)
    print(result)
    
    n = int(input('请输入数字：'))
    # 可尝试使用 eval(input()), 但是具有危险性，不建议使用
    s = n**3
    print(s)
    
    text = input('请发言：')
    print(test.textFilter(text))
    
    content = input('输入字符串：')
    t1 = time.time()
    content.swapcase()
    t2 = time.time()
    cost1 = t2 - t1

    t3 = time.time()
    test.convertToLower(content)
    t4 = time.time()
    cost2 = t4 - t3
    print(cost1, '\r\n', cost2)
    
    s1 = list(string.ascii_letters + string.digits+string.punctuation)
    rst = ''.join(list(random.choice(s1) for i in range(100)))
    print(rst)
    content = 'hehe, sha zi a ni heihei'
    pattern = re.compile(r'\b\w+i\b')
    print(pattern.search(content))
    '''




