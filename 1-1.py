#file = open("1-test.txt","r")
file = open("1.txt","r")
runningTotal = 0
elfs = []
for line in file:
    if len(line)>1: #1 for newline char)
        runningTotal += int(line.strip())
    else:
        elfs.append(runningTotal)
        runningTotal = 0
else:
    elfs.append(runningTotal)    
file.close()
print(max(elfs))