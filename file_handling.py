file = open('file_handling_test.txt', mode = "r") # generic way to open files with a permission(read in this case)

data = file.readline()

print(data)

file.close()


#-------------------------------------------------------------------

with open ('file_handling_test.txt', mode = "r") as file: # Newer, better way of handling files + is better at exception handling + automatically closes file
    data = file.readline()

    print(data)
    
#-------------writing to files and creating files-------------------
    
with open ('file_handling_new_file.txt', mode = "w") as file:
    file.write("This is a new file") # writes a single line

    file.writelines(["This is a new file \n", "This is another line"]) #Each string in the square brackets makes string of text, but it's actually the \n which makes a new line
