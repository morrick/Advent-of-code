#file = open("5-test.txt","r")
file = open("5.txt","r")

#load columns
maxCols = 9
columns = []
for i in range(maxCols):
    columns.append([])
for line in file:
    if len(line) <= 1 :
        break
    for i in range(maxCols):
        pos = line[(i*4)+1:(i*4)+2]
        if pos == "1":
            break
        if pos.strip():
            columns[i].insert(0,pos)
print(columns)

#load instruction 
for line in file:
    if len(line) <=1 :
        continue
    words = line.split()
    moves = int(words[1])
    fromCol = int(words[3])
    toCol = int(words[5])
    print(moves, fromCol, toCol)
    for move in range(moves):
        columns[toCol-1].append(columns[fromCol-1].pop())
print(columns)

for col in columns:
    print(col.pop(),end='')

file.close()