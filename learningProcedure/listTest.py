# 关于list的测试，包括少量的tuple，set，以及dict
l1 = list(i for i in range(101) if i % 2 == 0)
l2 = list(i for i in range(101) if i % 2 == 1)
l3 = list(a+b for a in l1 for b in l2 if a > 96 and b > 95)
print('l1: ', l1)
print('*'*120)
print('l2: ', l2)
print('*'*120)
print('l3: ', l3)
l4 = list(reversed(l3))
print('l4: ', l4)


a = [i for i in range(1, 6)]
print('原始的a:', id(a))
b = [i for i in range(6, 11)]
d = a + b
a.extend(b)
print('a: ', a)
print('现在的a:', id(a))
print('d: ', d)
print('现在的d:', id(d))


l5 = [i for i in range(1, 10)]
l6 = l5.copy()
l7 = l6[:]
print('l5: ', id(l5))
print('l6: ', id(l6))
print('l7: ', id(l7))


l8 = [i for i in range(1, 11)]
s1 = set(l8)
s1.discard(5)
print(l8)
print(l8.index(5))
print(l8.count(10))
d1 = dict.fromkeys(l8, 'Dave')
print(d1)