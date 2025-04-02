#Dictionary
#Dictionaries are used to store data values in key:value pairs,
#They are unordered, mutable(changeable) & don't allow duplicates
dict = {} #empty dictionary

dict = {
    "name" : "Sathwik",
    "learning" : "Coding",
    "languages" : ["Python", "C","Javascript"],
    "Courses" : ("AED", "DMDD", "DS", "ADS"),
    "age" : 29,
    "is_adult" : True,
    "gpa" : 3.7
}
print(dict["name"])
print(dict["learning"])
print(dict["languages"])
print(dict["Courses"])

dict["surname"] = "Hegde" #add new key and value

#Nested Dictionaries

student = {
    "name" : "Sathwik",
    "gpa" : {
            "DMDD" : 3.7,
            "ADS" : 3.6,
            "DS" :3.5
    }
}

print(student["gpa"]["DS"])

#Dictionary Methods
print(len(list(student.keys()))) #returns all key, typecast to list and return number of keys
print(len(list(student.values()))) #returns all values
print(list(student.items())) #returns all eky:values pairs

print(student["name"]) #error
print(student.get("name")) #no error --> none #returns the key according to value

student.update({
    "city" : "mumbai"
})                          #inerts the specified items to the dictionary

print(student)


#Set
'''Set is the collection of the unordered items
    Each element in the set must be unique and immutable'''

nums = {1,2,3,4}
set2 = {1,2,2,2}
print(nums)
print(set2)

collection = set() #emty set

#Set Methods
set2.add(5) # add an element
print(set2)
set2.remove(5) # remove an element
print(set2)

set2.clear() #clears the set
set2.pop() #removes a random element

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))
