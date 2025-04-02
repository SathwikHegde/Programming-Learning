#Chapter 1: Variables & Data Types

#Variables

name = "Sathwik Hegde"   #string
age = 25 #integer
school = "Northeastern University" #string
weight = 145.5 #float
height = 175.5 #float

print("Name:",  name, "Age:", age,"School:", school,"Weight:", weight, "Height:", height)

age2 =  age

print(age2) #STORING VALUE OF ONE VARIABLE INTO ANOTHER VARIABLE

#Data Types

print(type(name))
print(type(age))
print(type(school))
print(type(weight))
print(type(height))


age = 25
old = False
a =  None
print(type(old))
print(type(a))

#Keyowrds


#Print sum of 2 numbers
a = 5
b = 5
sum = a + b
print(sum)

#Print diff of 2 numbers
a = 5
b = 5
diff = a - b
print(diff)


#Expression Execution
#str * int
a,b = 2,3
txt = "@"
print (a*txt*b)

#str + str
a,b = "2",3
txt = "@"
print ((a+txt)*b)

#numeric values with  all arithmetic operators
a,b = 2,3
c= 4
print(a+b*c)

#arithmetic expression with integer and float will result in float
a,b = 10, 5.0
c=a*b
print(c)

#result of division operator with 2 integers will result in float
a,b = 1,2
c=a/b
print(c)

#integer division with float and int will give int displayed as float
a,b = 1.5,3
c=a//b
print(c,a/b)  #it will round off the o/p to closest float value

#Integer Division is same as "Floor" Function
#floor gives closest integer, which is lesser than or equal to float value
#Result of (A//B) is same as floor(A/B)

A,B =12,5
c=A//B
print(c)

A,B = -12,5
c=A//B
print(c)

A,B = 12,-5
c=A//B
print(c)


#Remainder is negative when denominator is negative
A,B = -5,2
c=A%B
print(c)

A,B = 5,2
c=A%B
print(c)

A,B =5,-2
c=A%B
print(c)

#Comments in python
# single line comment
"""This is 
multiple line
comment """

#Input in python
# input() statement is used to accept values(using Keyboard) from user

#string input
name = input("name: ")

#int input
age = int(input("age: "))

#float input
price = float(input("price: "))

print("My Name is", name, "and I am", age, "years old and my course price is", price)

#Run above code in a separate python program (ifelseTutorial.py)


#if else statement
if (condition):
    Statement1
elif (condition):
    Statement1
else: StatementN

#Run code examples in a separate python program (ifelseTutorial.py)

#conditional statements
# Single Line If/Ternary operators
# <var> = <val1> if <condition> else <val2>

food = input("food:")
eat = "YES" if food == "cake" else "no"
print(eat)

# <stm1>if<condition>else<stm2>
food = input("food:")
print("sweet") if food == "cake" or food == "icecream" else print("not sweet")

#Input
name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))
input()



