
__all__=['animal']
'''
__all__ 就是在form packageName import * 的时候生效。
正常情况下，使用form packageName import * 只会导入__init__模块中的所有内容，
但是有了__all__以后，就会调用其包含的模块名。除此以外的方法、函数都不会被调用了，但是直接的内容还是会被使用 — - >例如本页最后一句print('xixixixi')
'''
def haha():
    print('haha')

def inInit():
    print('hello world.')

print('xixixixi')