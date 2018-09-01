def add(a, b):
	print('ADDITION %d + %d' % (a,b))
	return a + b

def subtract(a, b):
	print('SUBTRACTION %d - %d' % (a, b))
	return a - b

def multiply(a, b):
	print('MULTIPLICATION %d * %d' % (a, b))
	return a * b

def divide(a, b):
	print('DIVISION %d / %d' % (a, b))
	return a / b

print('Let\'s perform several calculations using the function!')

age = add(30, 7)
height = subtract(190 , 4)
weight = multiply(35 ,2)
iq = divide(200, 2)

print('Age: %d, Height: %d, Weight: %d, IQ: %d' % (age, height, weight, iq))


#puzzle - additional task

print('This is puzzle.')

what = add(24, (subtract(divide(float(34), iq), multiply(iq,10.23))))

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))s

print('Is obtained:', what, 'You can calculate is manually?')

