#-*-coding:utf-8-*-
from sys import argv

#обьявляем аргументы
script, filename = argv

#парметру присваиваем функцию
txt = open(filename, 'r+')

#выводим текст
print 'File contents %r:' %filename
#вызываем функцию из переменной
#print txt.readline()
#print txt.readline()
print txt.truncate()

txt.close()

txt = open (filename, 'r+')
print 'Enter new text'
newtext = raw_input('> ')
file_new = txt.write(newtext)
txt.close()



#выводим текст
print 'Enter file\'s name again:'
#параметру присваеваем функцию для ввода текста с терминала
file_again = raw_input('> ')

#параметру присваеваем функцию
txt_again = open(file_again)

#вызываем функцию из переменной
print txt_again.read()
txt_again.close()