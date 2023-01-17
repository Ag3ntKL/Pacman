maze = open('assets/mazes/Maze1.txt').readlines()

for i in range(len(maze)):
    maze[i] = maze[i].split()

tempList = []
# Find the first and the last case
for i in range(len(maze)):
    for d in range(len(maze[i])):
        if maze[i][d] == '0' or maze[i][d] == '1':
            continue
        if maze[i][d] == 's':
            tempList.append((i, d))
        if maze[i][d] == 'e':
            end = (i, d)
        else :
            maze[i][d] = '1'
    # print(*maze[i])

rightWay = []
# Tester les directions
def VerifCase(tempList, index):
    possible = []
    """ if index < 10:
        print(f'tour : {index}  | {tempList}')
    else:
        print(f'tour : {index} | {tempList}') """
    for i in range(len(tempList)):
        # Droite
        if maze[tempList[i][0]][tempList[i][1]+1] == '0':
            maze[tempList[i][0]][tempList[i][1]] = True
            possible.append((tempList[i][0], tempList[i][1]+1))
        if maze[tempList[i][0]][tempList[i][1]+1] == 'e':
            rightWay.append(tempList)
            return 0
        # Gauche
        if maze[tempList[i][0]][tempList[i][1]-1] == '0':
            maze[tempList[i][0]][tempList[i][1]] = True
            possible.append((tempList[i][0], tempList[i][1]-1))
        if maze[tempList[i][0]][tempList[i][1]-1] == 'e':
            rightWay.append(tempList)
            return 0
        # Haut
        if maze[tempList[i][0]-1][tempList[i][1]] == '0':
            maze[tempList[i][0]][tempList[i][1]] = True
            possible.append((tempList[i][0]-1, tempList[i][1]))
        if maze[tempList[i][0]-1][tempList[i][1]] == 'e':
            rightWay.append(tempList)
            return 0
        # Bas
        if maze[tempList[i][0]+1][tempList[i][1]] == '0':
            maze[tempList[i][0]][tempList[i][1]] = True
            possible.append((tempList[i][0]+1, tempList[i][1]))
        if maze[tempList[i][0]+1][tempList[i][1]] == 'e':
            rightWay.append(tempList)
            return 0
    if possible == []:
        print('Le labyrinthe n\a pas de solution.')
        return 0
    rightWay.append(tempList)

    tempList = possible

    return VerifCase(tempList, index+1)

VerifCase(tempList, 0)
rightrightway = []
for i in range(len(rightWay), 0, -1):
    for d in rightWay[i-1]:
        if d[0] == end[0]+1 and d[1] == end[1]:
            rightrightway.append(d)
            end = d
        elif d[0] == end[0]-1 and d[1] == end[1]:
            rightrightway.append(d)
            end = d
        elif d[1] == end[1]-1 and d[0] == end[0]:
            rightrightway.append(d)
            end = d
        elif d[1] == end[1]+1 and d[0] == end[0]:
            rightrightway.append(d)
            end = d

rightrightway = rightrightway[::-1]
print(rightrightway)