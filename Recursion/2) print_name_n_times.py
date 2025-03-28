def printName(name, count):
    if count <= 5:
        print(name)
        printName(name, count+1)
        
name = "Aishwarya"
count = 1
printName(name, count)