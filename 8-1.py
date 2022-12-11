file = open("8-test.txt","r")
#file = open("8.txt","r")

rows,cols = 5,5 #test
#rows,cols = 99,99 #puzzle

forrest = ""
visibleFromEdge = 0

def getTree(row,col):
    return int(forrest[int(col)+(int(row)*cols)])

def isVisibleFromEdge(row,col):
    isVisible = False
    thisTree = getTree(row,col)
    #check to the north
    print("checking this: {} ({},{})".format(thisTree,row,col))
    # for n in range(row-1,-1,-1):
    #     targetTree = getTree(n,col)
    #     print("against this: {} ({},{})".format(targetTree,n,col))
    #     if int(targetTree) >= int(thisTree):
    #         print("target is larger or = than me")
    #     else:
    #         print("target is less than me")
            
    #check to the south
    # for s in range(row,rows):
    #     targetTree = getTree(s,col)
    #     print("against this: {} ({},{})".format(targetTree,s,col))
    #     if int(targetTree) >= int(thisTree):
    #         print("target is larger or = than me")
    #     else:
    #         print("target is less than me")

    #check to the east
    # for e in range(col,cols):
    #     targetTree = getTree(row,e)
    #     print("against this: {} ({},{})".format(targetTree,row,e))
    #     if int(targetTree) >= int(thisTree):
    #         print("target is larger or = than me")
    #     else:
    #         print("target is less than me")

    #check to the west
    # for w in range(col-1,-1,-1):
    #     targetTree = getTree(row,w)
    #     print("against this: {} ({},{})".format(targetTree,row,w))
    #     if int(targetTree) >= int(thisTree):
    #         print("target is larger or = than me")
    #     else:
    #         print("target is less than me")

    return isVisible
    

#load forrest
for line in file:
    forrest += line.strip()
#print(rows, cols, forrest)

#parse all trees in forrest
for i in range(rows):
    for j in range(cols):
        print("checking {} ({},{})".format(getTree(i,j),i,j))
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("is visible on edge")
            visibleFromEdge += 1
            continue
        if isVisibleFromEdge(i,j):
            visibleFromEdge += 1
print("visible from edge = ",visibleFromEdge)