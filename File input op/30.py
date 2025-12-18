with open("data.txt", "r") as file:
    data = file.read()
    if(data.find("python") != -1):
        print("Yes, 'python' is present.")
    else:
        print("No, 'python' is not present.")