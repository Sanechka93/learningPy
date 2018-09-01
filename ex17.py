from sys import argv 
from os.path import exists

script, from_file, to_file = argv

print 'Copy data from file %s to file %s' %(from_file, to_file) 

indata = open(from_file).read()

print 'The source file has a size %d bite' %len(indata)

print 'Destination file exists? %r' %exists(to_file)
print 'Ready for a work, press the Enter key to continue or CTRL+C to cancel.'
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print 'Excellent, everything done...'

out_file.close()
