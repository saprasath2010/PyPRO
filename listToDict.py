with open("spell.words.txt", "r") as f:
    newdict = {k.strip():1 for k in f.readlines()}

print (type(newdict))
print(newdict.items())
