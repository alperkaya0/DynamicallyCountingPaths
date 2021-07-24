
solvedOnes = {}
def countPaths(rows,columns,start):
    if start[0]>rows-1 or start[1]>columns-1:
        path = 0
    elif start[0] == rows-1 and start[1] == columns-1:
        path = 1
    else:
        if (tuple([start[0]+1,start[1]]) in solvedOnes) and (tuple([start[0]+1,start[1]+1]) in solvedOnes) and (tuple([start[0],start[1]+1]) in solvedOnes):
            path = solvedOnes[tuple([start[0]+1,start[1]])] + solvedOnes[tuple([start[0],start[1]+1])] + solvedOnes[tuple([start[0]+1,start[1]+1])]
        else:
            path = countPaths(rows,columns,[start[0]+1,start[1]]) + countPaths(rows,columns,[start[0],start[1]+1]) + countPaths(rows,columns,[start[0]+1,start[1]+1])
    solvedOnes[tuple(start)] = path
    return path


print(countPaths(5,5,[0,0]))
#print(len(str(shortestPath(2,2,[0,0]))))
