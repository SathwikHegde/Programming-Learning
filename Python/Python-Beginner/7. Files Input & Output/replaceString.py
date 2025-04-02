#WAF that replaces all the occurrences of "java" with "python" in above file

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("python", "javascript")
print(new_data)

with open("practice.txt", "w") as f:
    data = f.write(new_data)