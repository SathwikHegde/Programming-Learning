#Loops
#Loops are used to repeat instructions
 
count = 1
while count<=5:
    print("hello")
    count +=1
print(count)

#print number 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

#print number 5 to 1
i=5
while i>=1:
    print(i)
    i-=1

#Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#Print numbers 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#print multiplication table of number n
n = int(input("Enter a number: "))
i = 1
while i<=10:
    print(n*i)
    i+=1

#print the elements of the following list using a loop
nums = [1,4,9,16,25,36,49,64,81,100]

idx=0
while idx<len(nums):
    print(nums[idx]) #nums[0], nums[1]....
    idx+=1

#search for a number x in this tuple using loops
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i=0
while i<len(nums):
    if(x==nums[i]):
        print("found value: ", nums[i], "at index: ", i )
    else:
        print("not found at index: ", i)
    i+=1

#Break
'''used to terminate loop when encountered'''
i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

#Continue
'''terminates execution in the current iteration but continues execution of the loop with the next iteration'''

i = 1
while i<=5:
    if(i==3):
        i+=1
        continue #skip the remaining lines
    print(i)
    i+=1

#For Loops
'''Loops are used for sequential traversal. For traversing list, string, tuples etc.'''
num = [1,2,3,4,5]
for val in num:
    print(val)

tup = (1,2,3,4,5)
for val in tup:
    print(val)

str = "sathwikhegde"
for char in str:
    print(char)


str = "sathwikhegde"
for char in str:
    if(char=='k'):
        print("k")
        break
    print(char)
else:
    print("End")


#Print the elements of the following list using a loop:
nums = [1,4,9,16,36,49,64,81,100]
for val in nums:
    print(val)

#Search for number x in this tuple using loop:
nums = (1,4,9,16,36,49,64,81,100)
x = 36
idx = 0
for val in nums:
    if(val == x):
        print("Number Found at idx: ", idx)
        break
    idx+=1

#Range()
'''Range function returns a sequence of numbers, starting form 0 by default, and increments by 1(by default),
and stops before a specified number'''
#range(start, stop, step)
seq=range(5)
for i in seq:
    print(i)

for i in range(10): #range(stop)
    print(i)

for i in range(1,10): #range(start,stop)
    print(i)

for i in range(1,10,2): #range(start, stop, step)
    print(i)

#print even numbers
for i in range(2,100,2):
    print(i)

#print odd numbers
for i in range(1,100,2):
    print(i)

#print numbers from 1 to 100
for i in range(1,101):
    print(i)

#print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#print multiplication table of number n
n = 2
for i in range(1,11):
    print(i*n)

#Pass statement
'''pass is a null statement that does nothing. It is a placeholder for future code'''
for i in range(5):
    pass #can be used in try-catch and exceptions
print("This could to be completed in future")

#WAP to find the sum 1st n natural numbers
n=10
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum: ", sum)

n=10
sum=0
i=1
while i <= n:
    sum+=i
    i+=1
print("total sum: ", sum)

#WAP to find the factorial 1st n natural numbers

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial: ", fact)


n=5
fact=1
i=1
while i <= n:
    fact*=i
    i+=1
print("Factorial: ", fact)