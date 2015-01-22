#opening files

#1st method
#r = read w = write b = binary (useful on some systems)
#o_file = open('path/to/filename', 'rwb')
#file is now open and in memory as o_file
#to close a file use: o_file.close()

#example to play with:

o_file = open('method1.txt', 'w+')
print 'see that the open file is an object in memory:'
print o_file
o_file.write('First line\nSecond line\n')
o_file.close()
