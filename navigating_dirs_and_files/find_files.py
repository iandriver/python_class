#this file has examples of using the python os module for navigating directories and files
import os

print '\nPart 1:\n'
#the easiest way to go through all directories and files is os.walk
for root, dr, filename in os.walk('dirs_and_files'):
    #it walks down from the top directory
    print 'root = ', root
    print 'directory',  dr
    print 'filename =', filename
print '\nPart 2:\n'
    
for root, dr, filename in os.walk('dirs_and_files'):
    #parse and filter on root or dir or file (this is not universal, you must adapt to the file naming system)
    if '/' in root:
        f = root.split('/')[-1]
        print f
        print filename
        
print '\nPart 3:\n'
   
for root, dr, filename in os.walk('dirs_and_files'):
    if '/' in root:
        d = root.split('/')[-1]
        print d
        print filename
        for f in filename:
            #os.path.join will take arguments seperated by a comma and return a properly formated path
            with open(os.path.join(root,f), 'r') as fi:
                for line in fi:
                    print line 
                    
print '\nPart 4:\n'
    
for root, dr, filename in os.walk('dirs_and_files'):
    if '/' in root:
        d = root.split('/')[-1]
        print d
        print filename
        for f in filename:
            #os.path.join will take arguments seperated by a comma and return a properly formated path
            with open(os.path.join(root,f), 'r') as fi:
                for line in fi:
                    #a simple example of how you can navigate and find a file containing a specific string (in this case)
                    if line.split(' ')[-1] == '3':
                        print 'Found the path to file 3: '+os.path.join(root,f)                                   