import calendar


# calendar 测试
class MyCalendar(object):
    def __init__(self, year):
        self.printYear(year)
        print('{0} is leap year? '.format(year), calendar.isleap(year))
        print('how many leap years between 1949 to {0}? '.format(year), calendar.leapdays(1949, year))

    def printYear(self, n):
        cal = calendar.calendar(n)
        return cal


cal1 = MyCalendar(2018)
