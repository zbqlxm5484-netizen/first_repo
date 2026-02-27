n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
val =0
max_size = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > val :
            val = board[i][j]
for k in range(val+1):
    size = 0
    stack = []
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and not visited[i][j]:
                stack.append((i,j))
                visited[i][j] = 1
    
                while stack :
                    r,c = stack.pop()

                    for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ni,nj = r+di,c+dj
                        if 0 <= ni < n and 0 <= nj < n :
                            if board[ni][nj] > k and not visited[ni][nj]:
                                visited[ni][nj] = 1
                                stack.append((ni,nj))
                size += 1
    
    if size > max_size :
        max_size = size

print(max_size)