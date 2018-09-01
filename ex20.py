#-*-coding:utf-8-*-
from sys import argv
script, input_file = argv

#функция прочитать файл
def print_all(f):
    print f.read()

#функция поиска по файлу, 0 - указывает на начало файла
def rewind(f):
	f.seek(0)

#функция чтения одной строки с файла
def print_a_line(line_count, f):
	print line_count, f.readline()
#перемененной прсваиваем команду открыть файл
current_file = open(input_file)
#вывод текста
print 'First of all, we\'ll display this entire file: \n',
#вызываем функцию чтения файла 
print_all(current_file)
#вывод текста
print 'Now rewind, like a cassette.'
#вызываем функцию поиска по файлу
rewind(current_file)
#вывод текста
print 'Output three lines:'
#присваиваем переменной значение 1
current_line = 1
#вызываем функцию чтения по строке 
print_a_line(current_line, current_file)
#присваем перемееной предыдущее значение +1 и вызываем функцию чтения файла по строке
current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

