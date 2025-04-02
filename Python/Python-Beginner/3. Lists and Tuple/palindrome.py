#WAP program to check if a list contains a palindrome of elements.(Hint: use copy() method)

list1 = [1,2,2,1]
list2 = [1,"abc", "abc", 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if( copy_list1 == list1):
    print("List is palindrome")
else:
    print("List is not palindrome")


