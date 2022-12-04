#The first column is what your opponent is going to play:
# A for Rock, B for Paper, and C for Scissors.
#The second column, you reason, must be what you should play in response:
# X for Rock, Y for Paper, and Z for Scissors.
# for prt 2
# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win.
# Score
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def score(opponent, outcome):
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    tie = 3
    lose = 0
    if opponent == "A" and outcome == "X":
        return lose+scissors
    elif opponent == "A" and outcome == "Y":
        return tie+rock
    elif opponent == "A" and outcome == "Z":
        return win+paper
    elif opponent == "B" and outcome == "X":
        return lose+rock
    elif opponent == "B" and outcome == "Y":
        return tie+paper
    elif opponent == "B" and outcome == "Z":
        return win+scissors
    elif opponent == "C" and outcome == "X":
        return lose+paper
    elif opponent == "C" and outcome == "Y":
        return tie+scissors
    elif opponent == "C" and outcome == "Z":
        return win+rock


#file = open("2-test.txt","r")
file = open("2.txt","r")
cumulativeScore = 0
for line in file:
    perGameScore = 0
    plays = line.split()
    perGameScore += score(plays[0],plays[1])
    cumulativeScore += perGameScore
file.close()
print(cumulativeScore)