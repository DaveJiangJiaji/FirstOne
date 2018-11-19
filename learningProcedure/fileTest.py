import os
import json


class File(object):
    def __init__(self, path='/Users/superdrj/downloads'):
        os.chdir(path)

    def sortContent(self):
        with open('test.txt', 'r') as fp:
            data = fp.readlines()

            # 去掉空格
            data = [line.strip() for line in data]
            # 合并行，变成一个字符串
            data = ', '.join(data)
            # 将一个字符串分开，每个独立，这一步去除了文本中干扰的逗号
            data = data.split(',')
            # 将每个数字变成int，方便之后排序
            data = list(map(int, data))
            # 排序
            data.sort()
            # 完成排序后，恢复成string，方便写入文件
            data = ', '.join(map(str, data))
        return data

    def writeInto(self):
        with open('result,txt', 'w') as fp:
            fp.write(self.sortContent())

    def sortOnce(self):
        with open('test.txt', 'r') as src, open('newTest.txt', 'w') as rst:
            data = src.readlines()

            # 去掉空格
            data = [line.strip() for line in data]
            # 合并行，变成一个字符串
            data = ', '.join(data)
            # 将一个字符串分开，每个独立，这一步去除了文本中干扰的逗号
            data = data.split(',')
            # 将每个数字变成int，方便之后排序
            data = list(map(int, data))
            # 排序
            data.sort()
            data.reverse()
            # 完成排序后，恢复成string，方便写入文件
            data = ', '.join(map(str, data))
            rst.write(data)


class Calculate(object):

    def __init__(self):
        os.chdir('/Users/superdrj/downloads')
        self.loadFile()
        # loop: print(self.getLoopID())

    def loadFile(self):
        with open('test.json', 'r') as load_f:
            self.data = json.load(load_f)
            self.faces = self.data['faces']
            self.loops = self.data['loops']
            self.vertices = self.data['vertices']
            print(self.faces)
            print(self.loops)
            print(self.vertices)

    def getLoopID(self):
        outer = []
        inner = []
        for i in self.faces:
            if type(i['outer_loop']) is list:
                outer = i['outer_loop']
            else:
                outer.append(i['outer_loop'])
            if type(i['inner_loops']) is list:
                for j in i['inner_loops']:
                    inner.append(j)
            else:
                inner.append(i['inner_loops'])

        rst = outer + inner
        return rst

    def getVerticeID(self):
        pass


test = File()
test.writeInto()
test.sortOnce()





