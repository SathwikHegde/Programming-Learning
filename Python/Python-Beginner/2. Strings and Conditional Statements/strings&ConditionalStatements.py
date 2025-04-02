#***********************************#
str1 = "This is a string"
str2 = 'This is a string'
str3 = '''This is a string'''

#Escape sequence charater
str1 = "This is a string.\nWe are creating it in python."
#***********************************#
#Concatenation of strings
print(str1 + str2)

#Length of string
print(len(str1))
#***********************************#
#Indexing
Sathwik_Hegde
0123456789101112

str = "Sathwik_Hegde"
str[0] is 'S', str[1] is 'a'...
str[0] is 'B' #not allowed


str = "Sathwik_Hegde"
print(str[4])
#***********************************#

#Slicing
str = "SathwikHegde"
str[1 : 4] is "athw"
str[ : 4] is same as str[0 : 4] 
str[1 : ]  is same as str[1 :len(str)]

#Negative Index
Apple
-5-4-3-2-1
str = "Apple"
str[-3:-1] is "pl"

#String Functions
str = "i am a coder"
print(str.endswith("der")) #O/p will return True
print(str.capitalize()) #O/p will return True
print(str.replace("coder","programmer")) #replace old value with new value
print(str.find("am")) #returns 1st index of 1st occurrence
print(str.count("o")) #counts the occurrence of substring 

#Conditional Statements
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN


 


