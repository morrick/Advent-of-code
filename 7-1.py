#file = open("7-test.txt","r")
file = open("7.txt","r")

fileSystem = []
path = ""
newpath = ""
#turn the console commands into a data structure
for line in file:
    commands = line.split()
    if commands[0] == "$": #cli command
        if commands[1] == "cd": #change dir
            if commands[2] == "/":
                path = "/"
            elif commands[2] == "..":
                explode = path.split("+")
                explode.pop()
                newpath = ""
                for part in explode:
                    newpath += part
                    newpath += "+"
                newpath = newpath[:-1] #strip last +
                path = newpath
            else:
                path += "+"
                path += commands[2]
    elif commands[0] == "dir":
        fileSystem.append({
            "path":path,
            "name":commands[1],
            "type":"dir",
            "size":0
        })
    else:
        fileSystem.append({
            "path":path,
            "name":commands[1],
            "type":"file",
            "size":commands[0]
        })
#print(fileSystem)
#make a list of unique paths
list_of_paths = []
for node in fileSystem:
    list_of_paths.append(node.get("path")[-1:])
list_of_paths = list(set(list_of_paths))#de-duplicate list
size_list = {}
for path in list_of_paths:
    runningTotal = 0
    for node in fileSystem:
        if node.get("path").find(path) != -1: #path contains this folder
            runningTotal += int(node.get("size"))
    size_list.update({path:runningTotal})
#print(size_list)
total = 0
for item in list(size_list.keys()):
    if size_list.get(item) <= 100000:
        total += size_list.get(item)
print(total)