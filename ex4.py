
#-*-coding:utf-8-*-

#количество машин
cars = 100
#количество мест в машине
space_in_a_car = 4.0
#количество водителей
drivers = 30
#количество пассажиров
passengers = 90
#количество машин без водителя
cars_not_driven = cars - drivers
#количесвто машин с водителем
cars_driven = drivers
#сколько человек возможно перевезти
carpool_capacity = cars_driven * space_in_a_car
#среднее количество человек в одной машине
average_passengers_per_car = passengers / cars_driven

text = f'В наличии {cars} автомобилей'

print(text)

print("B наличии", cars, "автомобилей.")
print(f"B наличии, {cars}, автомобилей.")
#print u"И только", drivers, u"водителей вышли на работу."
#print u"Получается, что", cars_not_driven, u"машин пустуют."
#print u"Мы можем перевезти сегодня", carpool_capacity, u"человек."
#print u"Сегодня нужно отвезти", passengers, u"человек."
#print u"B каждой машине будет примерно", average_passengers_per_car, u"человека."

print ('текст')

