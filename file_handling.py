file = open('file_handling_test.txt', mode = "r") # generic way to open files with a permission(read in this case)

data = file.readline()

print(data)

file.close()


#-------------------------------------------------------------------

with open ('file_handling_test.txt', mode = "r") as file: # Newer, better way of handling files + is better at exception handling + automatically closes file
    data = file.readline()

    print(data)
    
#-------------writing to files and creating files-------------------
#NOTE: Writing in python removes the file's previous contents

with open ('file_handling_new_file.txt', mode = "w") as file:
    file.write("This is a new file") # writes a single line

    file.writelines(["This is a new file", "\nThis is another line"]) #Each string in the square brackets makes string of text, but it's actually the \n which makes a new line

#-----------------------appending to files--------------------------

#NOTE: Appending in python adds to the file's previous contents
    
with open ('file_handling_new_file.txt', mode = "a") as file:
    file.writelines(["This is a new file2", "\nThis is another line"])