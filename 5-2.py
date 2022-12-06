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
for line in file: #process the move instructions
    words = line.split()
    moves = int(words[1])
    fromCol = int(words[3])
    toCol = int(words[5])
    temp = []
    for move in range(moves):
        temp.append(columns[fromCol-1].pop())
    else:
        temp.reverse()
        columns[toCol-1].extend(temp)

#take the ends off and print them for a puzzle answer
for col in columns:
    print(col.pop(),end='')

file.close()