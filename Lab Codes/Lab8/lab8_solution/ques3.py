def hash_display():
    file = open("matter.txt","r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()

hash_display()
