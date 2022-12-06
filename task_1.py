#1.Вычислить число π c заданной точностью d
#*Пример:* 
#№ при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = float(input('введите d: '))
n = 3
s = math.pi
k = (1 - 1/n + 1/(n + 2))
pi2 = 4 * k
while pi2 - s  > d:
    pi2 = pi2 - 1/n + 1/(n + 2)
    n = n + 2 
    print(pi2)
print(math.pi)

'''
d = float(input('введите d: '))
a = 113355
b = a % 1000
c = a // 1000
pi_ = (b / c)
s = math.pi
if (pi_- s) < d:
    print(pi_)

#print(pi_)
print(math.pi)
'''

