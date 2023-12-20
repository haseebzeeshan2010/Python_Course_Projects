file = open('file_handling_test.txt', mode = "r") # generic way to open files with a permission(read in this case)

data = file.readline()

print(data)

file.close()


#-------------------------------------------------------------------

with open ('file_handling_test.txt', mode = "r") as file: # Newer, better way of handling files + is better at exception handling + automatically closes file
    data = file.readline()# NOTE: putting a number in the round brackets will mean that it will read only a specified number of characters on a line
    full_data = file.read() #Gets all of the text from a file
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

#-----------------------Splitting a files contents------------------

with open ('file_handling_test.txt', mode = "r") as file: # Newer, better way of handling files + is better at exception handling + automatically closes file
    
    full_data = file.read() #Gets all of the text from a file
    
    content_list = full_data.split("\n") #Split the text by \n
    print(content_list)