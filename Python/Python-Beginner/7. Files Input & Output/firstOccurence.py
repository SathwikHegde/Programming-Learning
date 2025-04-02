#WAF to find which line of the file does the word "learning" occur first. Print -1 if word not found

def search_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data  = f.read()
        if (word in data):
            print("Found")
        else:
            print("Found")

def search_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1
    return -1
print(search_line())