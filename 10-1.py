#file = open("10-test.txt","r")
file = open("10.txt","r")

X = 1
cycles = []

for line in file:
    if line.strip() == "noop":
        cycles.append(X)
    else:
        cycles.append(X)
        cycles.append(X)
        words = line.strip().split()
        X += int(words[1])
print(cycles)

numbers = [20,60,100,140,180,220]
total = 0
for num in numbers:
    total += num*cycles[num-1]
    print(num,cycles[num-1],num*cycles[num-1])
print(total)