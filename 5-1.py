#file = open("5-test.txt","r")
file = open("5.txt","r")

#load columns
maxCols = 9 #3 for test 9 for puzzle
columns = []
for i in range(maxCols): #fill the main list with empty lists per column
    columns.append([])

for line in file: #convert the puzzle input to lists
    if len(line) <= 1 : #on an empty line we're done
        break
    for i in range(maxCols):
        pos = line[(i*4)+1:(i*4)+2]
        if pos == "1": #break out on the column legend
            break
        if pos.strip(): #put the puzzle item into a list
            columns[i].insert(0,pos)

#load instruction 
for line in file:
    if len(line) <=1 :
        continue
    words = line.split()
    moves = int(words[1])
    fromCol = int(words[3])
    toCol = int(words[5])
    for move in range(moves):
        columns[toCol-1].append(columns[fromCol-1].pop())

for col in columns: #take the ends off the columns for the answer
    print(col.pop(),end='')

file.close()