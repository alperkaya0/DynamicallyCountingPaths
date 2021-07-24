
def countPaths(rows,columns,start):
    if start[0]>rows-1 or start[1]>columns-1:
        path = 0
    elif start[0] == rows-1 and start[1] == columns-1:
        path = 1
    else:
        path = countPaths(rows,columns,[start[0]+1,start[1]]) + countPaths(rows,columns,[start[0],start[1]+1]) + countPaths(rows,columns,[start[0]+1,start[1]+1])
    return path


print(countPaths(31,31,[0,0]))
