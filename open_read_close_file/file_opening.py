#opening files

#1st method
#r = read w = write b = binary (useful on some systems) + = editable, will write over existing
#o_file = open('path/to/filename', 'rwb+')
#file is now open and in memory as o_file
#to close a file use: o_file.close()

#example to play with:

o_file = open('method1.txt', 'rwb')
print 'see that the open file is an object in memory:'
print o_file
#write to file with .write I've already done this but the example is below
#o_file.write('First line\nSecond line\n')

#there are multiple ways to read a file but the easiest is to loop through it
line_list = []
for line in o_file:
    #strip() will remove new line \n
    l = line.strip()
    line_list.append(l)
    print l
print line_list

#with this method you must close the file or it will stay open in memory        
o_file.close()

#2nd method 
#use a with statement to open the file, it will close automatically when done

with open('method1.txt', 'rwb') as o2_file:
    print 'see that the open file is an object in memory:'
    print o2_file

    line_list = []
    for line in o2_file:
        #strip() will remove new line \n
        l = line.strip()
        line_list.append(l)
        print l
    print line_list
