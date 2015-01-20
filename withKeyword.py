with open("spell.words.txt", "r") as f:
    for i in f.readlines():
        print(i.strip())

print("The resource is no more available")
print(type(f))