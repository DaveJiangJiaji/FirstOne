import animal as ani
import learningProcedure.packageTest as test
import learningProcedure.exceptionCapture as ex



class Samoyed(ani.Dog):
    def __init__(self, name='小白', age=2, gender='Female', category='Dog', subCategory='Samoyed'):
        super(Samoyed, self).__init__(name, age, gender, category)
        self.setSubCategory(subCategory)

    def setSubCategory(self, subCategory):
        self._subCategory = subCategory

    def getSubCategory(self):
        return self._category


if __name__ == '__main__':
    s1 = Samoyed()
    s1.category()
    # 测试导入包中模块的功能。
    p1 = test.Package()
    e1 = ex.PrizeDraw()
