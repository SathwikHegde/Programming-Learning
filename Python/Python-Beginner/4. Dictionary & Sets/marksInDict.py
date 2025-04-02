'''WAP to enter marks for 3 subjects from the user and store them in a dictionary. 
   Start with an empty dictionary and add one by one, Use subjects name as key and marks as value '''


marks = {}

ads = input("Enter marks for ADS: ")
marks.update({"ADS" : 3.6})
dmdd= input("Enter marks for DMDD: ")
marks.update({"DMDD" : 3.7})
aed = input("Enter marks for AED: ")
marks.update({"AED" : 3.9})

print(marks)