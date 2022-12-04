#3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
#при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

lst = list(map(int, input('Введите элементы списка через пробел: ').split()))
print(lst)
unique_num = []
#lst = set(lst)
#print(set(lst))
#print(lst)
for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        unique_num.append(lst[i])
print(unique_num)