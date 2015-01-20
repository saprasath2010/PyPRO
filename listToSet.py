with open("spell.words.txt", "r") as f:
    newset = map(lambda i: i.strip(), f.readlines())

print (type(newset))
for i in newset:
    print(i)