#this file is a solution to problem 2 
import os
import pandas as pd

#Create lists to save all directories, files, and text in a list 
dirlist = []
samplist = []
textlist = []
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
        #open the file
        with open(path_to_file, 'rb') as txt_file:
            
            #each file has only one line so .readline() will work, you could also loop over the file with a for loop
            txt_id = txt_file.readline()
            #save each id as a list
            dirlist.append(sample_id)
            samplist.append(file_id)
            textlist.append(txt_id)
#create pandas dataframe with each dir name file and text
filename_df = pd.DataFrame({'Filename': samplist, 'text': textlist}, index = dirlist)
filename_df.index.name = 'Directory'
filename_df.to_csv('solution2_file_list.txt', sep = '\t')                         