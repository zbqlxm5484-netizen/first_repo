n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
path = []
visited = [False]*(n)
def dfs(depth) :
    if depth == m :
        print(*path)
        return
    
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            path.append(arr[i])

            dfs(depth+1)

            path.pop()
            visited[i] = False
dfs(0)