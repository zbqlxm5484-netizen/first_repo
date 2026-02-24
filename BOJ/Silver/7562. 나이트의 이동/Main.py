from collections import deque

for tc in range(1,int(input())+1) :
    n = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    visited = [[0]*n for _ in range(n)]
    visited[a][b] = 1
    dq = deque()
    dq.append((a,b))

    while dq :
        i,j = dq.popleft()
        if i == c and j == d :
            print(visited[i][j]-1)
            break

        for ni,nj in [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]] :
            di , dj = i + ni, j +nj
            if 0 <= di < n and 0 <= dj < n : 
                if not visited[di][dj] :
                    visited[di][dj] = visited[i][j] + 1
                    dq.append((di,dj))