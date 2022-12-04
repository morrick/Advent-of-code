#file = open("3-test.txt","r")
file = open("3.txt","r")
data = file.read().split("\n")
runningTotal = 0
for group in range(0,len(data),3):
    pack1 = data[group]
    pack2 = data[group+1]
    pack3 = data[group+2]
    charVal = ord(list(set(pack1)&set(pack2)&set(pack3))[0])
    if charVal < 97:
        runningTotal += charVal-64+26
    else:
        runningTotal += charVal-96
file.close()
print(runningTotal)
