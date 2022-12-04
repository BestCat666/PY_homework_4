#file = open(r'E:\PYhomework_4\task4.txt', encoding = 'utf-8')
#file = open('task4.txt','w', encoding = 'utf-8')
#print(file.read())  # читает весь файл
#print(file.read(2))  # отдельные символы, в том числе пробелы!
#print(file.read(2))  # начинает с того места, с которого закончил читать
#file.seek(0) # возвращает чтение на начало файла
#print(file.read(2))
#print(file.readline()) # читает строчку целиком
#for row in file:       # читает по строкам
#   print(row)

#for row in file:          # читает по буквам
#    for letter in row:
#        print(letter)

#s = file.readlines()    #превращает в список
#print(s)


file = open('task4.txt','w', encoding = 'utf-8')
file.write('lololo')

file = open('task4.txt','a', encoding = 'utf-8')
file.write('rhrhrhr')

file = open('task4.txt','a+', encoding = 'utf-8')  #режим записи и чтения
file.write('rhrhrhr')

file.close()