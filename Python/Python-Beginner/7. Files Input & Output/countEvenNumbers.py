#From a file containing numbers separate by comma, print the count of even numbers 

# with open("numbers.txt", "r") as f:
#     data = f.read()
#     print(data)


    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #     else:
    #         num += data[i]

    
count =0
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val)%2 ==0):
            count+=1
        
print(count)