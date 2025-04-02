#Traffic light Example
"""light = input("Color: ")
if (light == "red"):
    print("Stop")
elif (light == "yellow"):
    print("look")
elif (light == "green"):
    print("go")
else: print("traffic light is broken") """

#Grade example
"""marks = int(input("marks: "))
if (marks >= 90):
    print("grade A")
elif (marks >= 80 and marks < 90):
    print("grade B")
elif (marks >= 70 and marks < 80):
    print("grade C")
else: print("grade D")"""

# Print output for 1) A = 5 & G = M ; 2) A = 2 & G = F
A= int(input("A: "))
G= input("M/F: ")
if ((A == 1 or A == 2) and G == "M"):
    print ("Fee is 100")
elif ((A == 3 or A == 4) and G == "F"):
    print ("Fee is 200")
elif (A == 5 and G == "M"):
    print ("Fee is 300")
else:
    print("no fee")

# Single line If/ Ternary operator
#Syntax 1
<var> = <val1> if <condition>else<val2>

food = input("food:")
eat = "Yes" if food == "cake"else"no"
print(eat)

#Syntax 2
<stt1> if<condition>else<stt2>
food = input("food:")
print("sweet") if food ==  "cake" or food == "icecream" else print("not sweet")

# Clever If/ Ternary operator

<var> = (false_val,true_val)<condition>

age = int(input("age:"))
vote = ("yes","no")[age<18]

sale = float(input("salary:"))
tax = sal*(0.1,0.2) [sal<=50000]
print(tax)


