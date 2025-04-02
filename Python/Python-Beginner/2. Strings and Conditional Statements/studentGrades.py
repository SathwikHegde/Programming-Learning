#WAP to identify grades of a student

marks = int(input("Enter your Marks:"))
if(marks>= 90):
    print("You scored Grade A")
elif(marks<90 and marks>80):
    print("You scored Grade B")
elif(marks<80 and marks>70):
    print("You scored Grade C")
else:
    print("You scored Grade D")
