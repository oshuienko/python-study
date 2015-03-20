#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

# окрытие файла с данными и преобразование их в словарь
put = '/home/norbert/Python_study/words_1.txt'
words = {}
for line in open(put):
    line = line.split('\n')    # избавляемся от последнего элемента (\n)
    line = line[0]             # из строки получаем список
    line = line.split('|')     # разделяем данные                   
    words[line[0]] = line[1]   # добавляем в словарь                           
    words[line[1]] = line[0]   # первый элемент списак - как ключ,остальные - значение

print 'New_words: ' + str(len(words)) #кол-во слов для изучения
                             
                               
#Тело программы
print ('\n')                        #переход на новую строку ч/з enter
error = []
errorb = [] 
k = 0                               
s = 0                               #Обнуление переменной счетчика
col = 1                                      
while words: 
    c = words.keys()                         #Вывод ключей словаря
    a = random.choice(c)                     #Вывод случайного ключа из словаря
    print str(col) + ' - ' + str(a)
    col += 1                                 #Вывод зн-ния user
    b = raw_input('Please, translate:  ')  #Ввод со стороны user значения
    d = words.values()
     
    if b == words[a]:                        #проверка ввода 
        print('Good')
        s += 1    
    else:
        print('Bad!')
        k +=1
        error.append(a)
        errorb.append(b)                     
    words.pop(a)                             #удаление элемента со словаря
    print ('\n')

print 'Results_Good!: ' + str(s)
print 'Results_Bad!: ' + str(k) + '\n'


for i in error:  # вывод результата в столбик
    print('- '+ i)

print ('\n')
for i in errorb:
    print('- '+ i)
