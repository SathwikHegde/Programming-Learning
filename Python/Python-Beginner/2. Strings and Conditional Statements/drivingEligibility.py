#WAP to identify if the candidate is eligible for Drivers license

Age = int(input("Enter your Age:"))
if(Age >= 18):
    if(Age > 80):
        print("You are Ineligible")
    else:
        print("You are Eligible")
else:
    print("You are Ineligible")
