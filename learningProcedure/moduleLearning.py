import calendar
import time


# calendar 测试
class MyCalendar(object):
    def __init__(self, year):
        self.printYear(year)
        print('{0} is leap year? '.format(year), calendar.isleap(year))
        print('how many leap years between 1949 to {0}? '.format(year), calendar.leapdays(1949, year))

    def printYear(self, n):
        cal = calendar.calendar(n)
        return cal


if __name__ == '__main__':
    cal1 = MyCalendar(2018)
    print(time.timezone)
    str1 = input('请输入一串字符：')
    rst = []
    for i in str1:
        if 'A' <= i <= 'Z':
            s = i.lower()
            rst.append(s)
        else:
            rst.append(i)
    result = ''.join(rst)

    print(result)
