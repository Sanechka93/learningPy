#-*-coding:utf-8-*-

formatter = '%s %s %s %s'

print(formatter % (1,2,3,4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % 
	('Sleep in a stable pony,',
	'the dog began to doze,',
	'only Johnny\'s boy',
	'does not go to sleep!'))
