#1.Вычислить число π c заданной точностью d
#*Пример:* 
#№ при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = float(input('введите d: '))
n = 1
a = 4
b = 1
s = math.pi
pi = a  * (b - (1/(2 * n + 1)) * ((-1)**n))
while (pi - s)  > d:
    k = b - (1/(2 * n + 1)) * ((-1)**n)
    pi = a * k
    n = n + 1 
print(pi)
print(math.pi)

'''q
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

