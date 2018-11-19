import os


os.chdir('/Users/superdrj/downloads')


def formatData(src, dst):
    with open(src, 'r', encoding='utf-8') as src, open(dst, 'w', encoding='utf-8') as dst:
        lines = src.readlines()
        list_1 = []
        for line in lines:
            if line not in list_1 and len(line.split(',')) == 5:
                list_1.append(line)
                dst.write(line)


if __name__ == '__main__':
    formatData('xie_zheng.txt', 'new_data.txt')
