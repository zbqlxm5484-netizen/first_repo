n = int(input())
board = [list(input().strip()) for _ in range(n)]

temp = [row[:] for row in board]

for i in range(n):
    for j in range(n):
        if temp[i][j] == "R" :
            temp[i][j] = "G"
size = 0
dsize = 0
stack = []
visited = [[0]*n for _ in range(n)]
dvisited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == "R" and not visited[i][j]:
            stack.append((i,j))
            visited[i][j] = 1
            

            
            while stack :
                r,c = stack.pop()

                for ni ,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                    di,dj = ni+r,nj+c
                    if 0 <= di < n and 0 <= dj < n :
                        if board[di][dj] == "R" and not visited[di][dj] :
                            visited[di][dj] = 1
                            stack.append((di,dj))
            else :
                size += 1
for i in range(n):
    for j in range(n):
        if board[i][j] == "G" and not visited[i][j]:
            stack.append((i,j))
            visited[i][j] = 1
            

            
            while stack :
                r,c = stack.pop()

                for ni ,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                    di,dj = ni+r,nj+c
                    if 0 <= di < n and 0 <= dj < n :
                        if board[di][dj] == "G" and not visited[di][dj] :
                            visited[di][dj] = 1
                            stack.append((di,dj))
            else :
                size += 1
for i in range(n):
    for j in range(n):
        if board[i][j] == "B" and not visited[i][j]:
            stack.append((i,j))
            visited[i][j] = 1
            

            
            while stack :
                r,c = stack.pop()

                for ni ,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                    di,dj = ni+r,nj+c
                    if 0 <= di < n and 0 <= dj < n :
                        if board[di][dj] == "B" and not visited[di][dj] :
                            visited[di][dj] = 1
                            stack.append((di,dj))
            else :
                size += 1
for i in range(n):
    for j in range(n):
        if temp[i][j] == "B" and not dvisited[i][j]:
            stack.append((i,j))
            dvisited[i][j] = 1
            

            
            while stack :
                r,c = stack.pop()

                for ni ,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                    di,dj = ni+r,nj+c
                    if 0 <= di < n and 0 <= dj < n :
                        if temp[di][dj] == "B" and not dvisited[di][dj] :
                            dvisited[di][dj] = 1
                            stack.append((di,dj))
            else :
                dsize += 1                
for i in range(n):
    for j in range(n):
        if temp[i][j] == "G" and not dvisited[i][j]:
            stack.append((i,j))
            dvisited[i][j] = 1
            

            
            while stack :
                r,c = stack.pop()

                for ni ,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                    di,dj = ni+r,nj+c
                    if 0 <= di < n and 0 <= dj < n :
                        if temp[di][dj] == "G" and not dvisited[di][dj] :
                            dvisited[di][dj] = 1
                            stack.append((di,dj))
            else :
                dsize += 1                
print(size, dsize)
