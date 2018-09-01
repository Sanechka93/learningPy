from sys import argv

script, user_name, surname = argv
answer = 'Enter answer: '

print 'Hello %s %s, I am script %r.' % (user_name, surname, script)
print 'I have some quetions for you.'
print 'Do you like me, %s %s?' %(user_name, surname) 
likes = raw_input(answer)
print 'Where do you live, %s %s?' %(user_name, surname)
lives = raw_input(answer)
print 'What computer do you work on?'
computer = raw_input(answer)

print '''
So, your answered %r to the question, do I like you.
You live in %r. I do not know where it is.
And you have a computer %r. Perfectly! 
''' %(likes, lives, computer)