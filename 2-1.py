#The first column is what your opponent is going to play:
# A for Rock, B for Paper, and C for Scissors.
#The second column, you reason, must be what you should play in response:
# X for Rock, Y for Paper, and Z for Scissors.
# Score
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

#file = open("2-test.txt","r")
file = open("2.txt","r")
cumulativeScore = 0
for line in file:
    perGameScore = 0
    plays = line.split()

    if (plays[0] == "A" and plays[1] == "Y") or (plays[0] == "B" and plays[1] == "Z") or (plays[0] == "C" and plays[1] == "X"):
        perGameScore += 6 #win
    elif (plays[0] == "A" and plays[1] == "X") or (plays[0] == "B" and plays[1] == "Y") or (plays[0] == "C" and plays[1] == "Z"):
        perGameScore += 3 #tie
    elif (plays[0] == "A" and plays[1] == "Z") or (plays[0] == "B" and plays[1] == "X") or (plays[0] == "C" and plays[1] == "Y"):
        perGameScore += 0 #loss

    if plays[1] == "X": #played rock
        perGameScore += 1
    elif plays[1] == "Y": # played paper
        perGameScore += 2
    elif plays[1] == "Z": # played scisors
        perGameScore += 3

    cumulativeScore += perGameScore
file.close()
print(cumulativeScore)