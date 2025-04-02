#Lists
'''A Built-in Datatype that stores the set of values.
   It can store elements of different types(integer, float, string, etc.)'''

student =  ["Sathwik", "M", 29, "Mumbai"]
student[0] = "Hegde" #lists are mutable

#List Slicing
list_name[starting_index:ending_index]; #ending index is not included
marks = [87,64,33,95,76]
marks[1:4] is [64,33,95]
marks[:4] is [87,64,33,95]
marks[1:] is [64,33,95,76]
marks[-3,-1] is [33, 95]


#List Methods
list = [2,1,3]

list.append(4) #appends an element to the end
list.sort() #sorts the list in asc order
list.sort(reverse=True) #sorts the list in desc order
list.reverse() # reverses the list
list.insert(idx, el) # inserts element at index
list.remove(1) #removes the first occurrence of the element
list.pop(idx) #removes element at idx


#Tuples 
'''A built in data type that lets us create immutable sequence of values'''
tup = (2,1,2,3)
print(tup[0])
print(tup[1])
print(tup[1:3])

#Tuple Methods
tup = (2,1,3,1)

tup.index(el) #returns index of first occurrence tup.index(1) is 1
tup.count(el) #counts total occurrences tup.count(1) is 2