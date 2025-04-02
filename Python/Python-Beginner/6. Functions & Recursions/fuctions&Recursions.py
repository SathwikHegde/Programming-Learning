#Functions
'''Block of statements that perform a specific task'''
'''def func_name(param1, param2):  #function definition
        #some work
        return val
        
func_name(arg1,arg2)..function call'''

def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(5,10)
calc_sum(12,17)
calc_sum(12,25)


def calc_sum(a,b):
    return a+b
sum = calc_sum(1,2)
print(sum)


def print_hello():
    print("Hello")
print_hello()

#Create a function to calculate avg of 3 numbers

def cal_avg(a,b,c):
    return (a+b+c/3)
avg= cal_avg(2,4,6)
print(avg)

#default parameters
def cal_prod(a=1,b=1): #assigning default values
    print(a*b)
    return(a*b)
cal_prod()


#WAF to print the length of the list(list is a parameter)
nums = [1,2,3,4,5]
cities = ["mumbai", "delhi", "bangalore", "chennai"]
def length(list):
    print(len(list))
length(nums)
length(cities)


#WAF to print the elements of a list in a single line.(list is the parameter)
nums = [1,2,3,4,5]
cities = ["mumbai", "delhi", "bangalore", "chennai"]

def print_elements(list):
    for item in list:
        print(item, end=" ")
print_elements(cities)


#WAF to find the factorial of n. (n is the parameter)

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)
fact(5)

#WAF to converts usd to inr

def conv(usd):
    inr = usd * 84
    print("USD= $",usd, "INR = Rs", inr )
conv(5)


#WAF to take input numb and return if it  is odd or even

num = 2

def num_type(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num_type(num)


#Recursion
'''When a function calls itself repeatedly'''
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

#Factorial using recursion
def fact(n):
    if(n == 1 or n==0):
        return 1
    return fact(n-1) * n
print(fact(4))

#Write a recursive function to calculate the sum of first n natural numbers
def sum_val(n):
    if(n==0):
        return 0
    return sum_val(n-1) + n
sum=sum_val(5)
print(sum)

#Write a recursive function to print all elements in a list. (Use list and index aas parameters)
def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx +1)

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)