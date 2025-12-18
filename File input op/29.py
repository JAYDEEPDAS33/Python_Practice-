with open ("data.txt", "r") as file:
    data = file.read()
new_data = data.replace("python", "java")
print(new_data)