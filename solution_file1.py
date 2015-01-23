#this file is a solution to problem 1 
import os

#walk over all of the files in 'file_py_test'
for root, dr, filename in os.walk('file_py_test'):
    #create a way to select the files you want since all of the files have Sample_, I used that
    if 'Sample_' in root:
        #parse the 6 digit string from the directory (sample) and file and save each id
        sample_id = root.split('/')[-1].split('_')[-1]
        file_id = filename[0].strip('.txt').split('_')[-1]
        #since filenames are in lists and there is only one file, take the filename out of the list and save it as a string
        f_name_string =  filename[0]
        #create a usable path to each file
        path_to_file = os.path.join(root, f_name_string)
        #the in text string to find
        string_to_find = '8IPLEQ'
        #open the file
        with open(path_to_file, 'rb') as txt_file:
            #each file has only one line so .readline() will work, you could also loop over the file with a for loop
            txt_id = txt_file.readline()
            #if the text in the file matchs the sting to find print out the sample and file ids
            if txt_id == string_to_find:
                print 'The string', string_to_find, 'is in:'
                print 'Sample id:', sample_id
                print 'File id:  ', file_id                            