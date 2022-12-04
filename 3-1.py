#file = open("3-test.txt","r")
file = open("3.txt","r")
runningTotal = 0
for line in file:
    middle = int(len(line.strip())/2)
    match = set(line[:middle])&set(line[middle:])
    charVal = ord(list(match)[0])
    if charVal < 97:
        runningTotal += ord(list(match)[0])-64+26
    else:
        runningTotal += ord(list(match)[0])-96
print(runningTotal)
file.close()