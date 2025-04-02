#Search if the word learning exists in the file or not
def search_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data  = f.read()
        if (data.find(word) != -1):
            print("Found")
        else:
            print("Found")
search_word()