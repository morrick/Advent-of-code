#file = open("4-test.txt","r")
file = open("4.txt","r")
runningTotal = 0
for line in file:
    elfs = line.strip().split(",")
    elf1range = elfs[0].split("-")
    elf2range = elfs[1].split("-")
    elf1set = set(range(int(elf1range[0]),int(elf1range[1])+1))
    elf2set = set(range(int(elf2range[0]),int(elf2range[1])+1))
    if len(elf1set&elf2set) > 0:
    #if elf1set.issubset(elf2set) or elf1set.issuperset(elf2set):
        runningTotal += 1
print(runningTotal)
file.close()