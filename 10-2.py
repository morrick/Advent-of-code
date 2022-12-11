#file = open("10-test.txt","r")
file = open("10.txt","r")

X = 1
cycles = []
crt = []
for line in file:
    if line.strip() == "noop":
        cycles.append(X)
        if (len(cycles)-1)%40 in range(X-1,X+2,1):
            crt.append("#")
        else:
            crt.append(".")

    else:
        cycles.append(X)
        if (len(cycles)-1)%40 in range(X-1,X+2,1):
            crt.append("#")
        else:
            crt.append(".")
        cycles.append(X)
        if (len(cycles)-1)%40 in range(X-1,X+2,1):
            crt.append("#")
        else:
            crt.append(".")
        words = line.strip().split()
        X += int(words[1])
#print(cycles)

count = 0
for pixel in crt:
    count += 1
    print(pixel,end="")
    if count%40==0:
        print()


numbers = [20,60,100,140,180,220]
total = 0
for num in numbers:
    total += num*cycles[num-1]
    #print(num,cycles[num-1],num*cycles[num-1])
#print(total)