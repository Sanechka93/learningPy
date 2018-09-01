from sys import argv

script, filename = argv

print 'I\'m going to erase the file %r.' %filename
print 'If you do not want to erase it, press the key combination CTRL+C (^C).'
print 'If you want to erase file, press Enter key.'

raw_input('?')

print 'Opening a file...'
target = open(filename, 'w')

print 'Clearing the file. Bye!'
target.truncate()

print 'Now I ask you for three lines.'

line1 = raw_input('line 1: ')
line2 = raw_input('line 2: ')
line3 = raw_input('line 3: ')

print 'This I will write to the file.'

target.write('%s\n%s\n%s' %(line1,line2,line3))
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

#print 'And finally, I will close the file.'
target.close()

target = open(filename, 'r+')
print target.read()
target.close()

