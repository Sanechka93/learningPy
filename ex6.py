#-*-coding:utf-8-*-

x = "Существует %d типов людей." % 10
binary = "Python"
do_not = "нет"
y = "Te, кто понимает %r, и те, кто — %s." % (binary, do_not)

print (x)
print (y)

print ("Я сказал: %s." % x)
print ("A еще я сказал: ' %s'." % y)

hilarious = False
joke_evaluation = "Разве это не смешно?! %r"

print (joke_evaluation % hilarious)

w = "Это часть строки слева..."
e = " а это справа."

print (w + e)