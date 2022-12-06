#4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#*Пример:* 
#k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
k = int(input('Введите натуральную степень k: '))
lst = [f'{randint(-100,100)}x**{k}']
for i in range(k - 1):
    if randint(0, 25) > k:
        lst.append(f'{randint(-100,100)}x**{i}')
print(lst)
temp = ' '.join(lst)
#print(t)
temp = '+'.join(temp.split())
#print(t)
if '+-' in temp:
    polynomial = temp.replace('+-', ' - ')
file = open('task4.txt','w')
file.write(polynomial)
file.close()

'''
else:
    file = open('task4.txt','w')
    file.write(' + '.join(t) + ' = 0')
    file.close()

exit()

print(s.replace('o', '%'))

file = open('task4.txt','w')
file.write(' + '.join(lst) + ' = 0')
file.close()



import random
k = int(input('Введите натуральную степень k: '))
coeff = [random.randint(0,100) for i in range(k + 1)]
print(coeff)
for j in range(len(coeff) - k):
    polynomial = f'{coeff[j]}*x^{k}'
    k = k - 1
    j = j + 1
    polynomial = polynomial + '+' + f'{coeff[j]}*x^{k}'
    j = j + 1
    k = k - 1
    polynomial = polynomial +  '+' + f'{coeff[j]} = 0'
    j = j + 1     
    print(polynomial)

file = open('task4.txt','w')
file.write(polynomial)
file.close()
'''