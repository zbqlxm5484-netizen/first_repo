from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dq = deque()
stack = deque ()
year = 0
size = 0
visited = [[0]*m for _ in range(n)]
flag = False
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and not visited[i][j] :
            stack.append((i,j))
            visited[i][j] = 1
            size += 1
            while stack :
                si,sj = stack.pop()
                

                for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                    di,dj = ni+si,nj+sj
                    if 0 <= di < n and 0 <= dj < m :
                        if not visited[di][dj] and board[di][dj] != 0 :
                            visited[di][dj] = 1
                            stack.append((di,dj))
while size <= 1:
    row = [[0]*m for _ in range(n)]
    max_size = 0
    year += 1
    if sum(board[i][j]for i in range(n) for j in range(m)) == 0 :
                break
    
    for i in range(n):
        for j in range(m):
            

            if board[i][j] != 0 :
                dq.append((i,j))
                

                while dq :
                    r,c = dq.popleft()

                    for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                        sr,sc = r+x,c+y
                        if 0 <= sr < n and 0 <= sc < m :
                            if board[sr][sc] == 0 and board[i][j] != "del" :
                                board[i][j] = board[i][j] - 1
                                if board[i][j] <= 0 :
                                    board[i][j] = "del"
                                    visited[i][j] = 0
                                
    for i in range(n):
        for j in range(m):
            if board[i][j] == "del" :
                board[i][j] = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not row[i][j] :
                stack.append((i,j))
                row[i][j] = 1
                max_size += 1
                
                while stack :
                    si,sj = stack.pop()

                    for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]] :
                        di,dj = ni+si,nj+sj
                        if 0 <= di < n and 0 <= dj < m :
                            if not row[di][dj] and board[di][dj] != 0 :
                                row[di][dj] = 1
                                stack.append((di,dj))
    if max_size > size :
        size = max_size
        flag = True
        break

if flag :
    print(year)
else :
    print(0)
            