string = "hello world"

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substring = string[i:j]
        print(substring)