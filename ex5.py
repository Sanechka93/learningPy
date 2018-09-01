#-*-coding:utf-8-*-

name = 'Sanechka'
age = 24 
height = 168 # см
weight = 55 # кг
eyes = 'Зеленые'
teeth = 'Белые'
hair = 'Черные'

print("Давайте поговорим о человеке по имени %s." % name)
print("Ее рост составляет %d см." % height)
print("Она весит %d кг." % weight)
print("Ha самом деле это не так и много.")
print("У нее %s глаза и %s волосы." % (eyes, hair))
print("Ее зубы обычно %s, хотя она и любит пить кофе." % teeth)

# эта строка кода довольно сложная, не ошибитесь!
print("Если я сложу %d, %d и %d, то получу %d." % (age, height, weight, age + height + weight))