#File I/O in Python

'''Python can be used to perform operations on a file. (read & write data)'''

'''Types of all files 
1. text Files: .txt, .log, .docx
2. Binary Files: .mp4, .mov, .png, .jpeg'''

#open, read and close file

'''we have to open  file before reading and writing'''

f = open("file_name", "mode")         
data =f.read
f.close()


f = open("demo.txt","r")
data =f.read()
print(data)
print(type(data))
f.close()

# Reading a file
data =f.read() #read entire file
data =f.readline() #reads one line at a itme

#Writing to a file
f = open("demo.txt", "w")
f.write("I want to start learning javascript tomorrow") #overwrites the entire file
f = open("demo.tx", "a")
f.write("this is a new line") #adds to the file


#With Syntax

with open("demo.txt", "a") as f:
    data = f.read()
    print(data)

with  open("demo.txt", "w") as f:
    f.write("new data")

#Deleting a file

#deleting a file
'''
using th OS module.
Module(like a code library) is a file written by another programmer that generally has a function we can use.
'''
import os
os.remove("sample.txt")