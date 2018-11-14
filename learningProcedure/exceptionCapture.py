import random


class PrizeDraw(object):
    '''
    这是一个猜幸运数字的小程序，它会让你一直猜数字，直到你猜对。
    每错误一次，就会更新一次新的幸运数字列表。
    每次列表内有10个幸运数字，每个幸运数字在0到1104之间（不包括1104）
    '''
    def __init__(self):
        self.guessing()

    def setMagicNum(self):
        self.__magicNum = list(random.randint(0, 1104) for i in range(10))

    def getMagicNum(self):
        return self.__magicNum

    def guessing(self):
        flag = True
        while flag:
            try:
                self.setMagicNum()
                n = int(input('请输入一个整数：'))
                print('本次的幸运数字有：', self.getMagicNum())

                for i in self.getMagicNum():
                    if i == n:
                        print('恭喜你，猜对了。隐藏的幸运数字为：{0}'.format(self.getMagicNum()))
                        flag = False
                        break

                signal = input('抱歉，没能猜对本轮的幸运数字。请问是否还要继续，输入yes/no:')
                if signal.lower() == 'no':
                    break

            except ValueError as e:
                print('请输入正确的数字，谢谢。')
                print(e)
                print('*'*163)

            except Exception as e:
                print('搞啥呢兄弟？')
                print(e)
                print('*'*163)


class RaiseError(object):
    '''
    上面的class使用了try except
    这个class则是用了raise语句，主动提出异常。
    '''
    def __init__(self):
        self.test()

    def test(self):
        try:
            print('我测试一下raise咋用')
            raise ValueError
            print('正常情况下，这句话不会被看到。')
        except NameError as e:
            print('Name error, bro.')
            print(e)
        except ValueError as e:
            print('Value error, m8.')
            print(e)
        except Exception as e:
            print(e)
        finally:
            print('我是收尾工作。')


if __name__ == '__main__':
    prizeDraw = PrizeDraw()
    print('本轮抽奖结束～')
    test = RaiseError()
    exit()
    print('看不见我，啦啦啦～～～')





