maze = open('assets/mazes/Maze1.txt').readlines()

for i in range(len(maze)):
    maze[i] = maze[i].split()

coordTab = [(i,d) for i in range(len(maze)) for d in range(len(maze[i])) if maze[i][d] == '0']

tempList = []
# Find the first and the last case
for i in range(len(maze)):
    for d in range(len(maze[i])):
        if maze[i][d] == 's':
            start = (i, d)
            tempList.append(start)
        if maze[i][d] == 'e':
            end = (i, d)
    print(*maze[i])

finish = True
rightWay = []

# Tester les directions
def VerifCase(tempList):
    for i in range(len(tempList)):
        possible = []
        # Droite
        if maze[tempList[i][0]][tempList[i][1]+1] == '0':
            possible.append((tempList[i][0], tempList[i][1]+1))
        # Gauche
        if maze[tempList[i][0]][tempList[i][1]-1] == '0':
            possible.append((tempList[i][0], tempList[i][1]-1))
        # Haut
        if maze[tempList[i][0]-1][tempList[i][1]] == '0':
            possible.append((tempList[i][0]-1, tempList[i][1]))
        # Bas
        if maze[tempList[i][0]+1][tempList[i][1]] == '0':
            maze[tempList[i][0]][tempList[i][1]] = True
            possible.append((tempList[i][0]+1, tempList[i][1]))

        if len(possible) == 1:
            rightWay.append(possible[0])
            tempList = possible
    if len(possible) == 1:
        return VerifCase(tempList)

VerifCase(tempList)

print("\n\n")
for i in range(len(maze)):
    print(*maze[i])

print(rightWay)