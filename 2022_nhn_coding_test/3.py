maze=["AAAAA", "AABBB", "CAEFG", "AAEFF"]
queries=["1 1 1 5 AF", "1 1 4 5 AF", "2 1 4 5 FAE", "1 5 4 5 ABF", "1 1 4 1 A"]
maze=["00000"]+maze
for i in range(len(maze)):
    maze[i]="0"+maze[i]
    print(maze[i])
# 포기