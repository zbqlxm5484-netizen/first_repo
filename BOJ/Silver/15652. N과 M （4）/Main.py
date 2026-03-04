n,m = map(int,input().split())
path = []

def dfs(depth):
    if depth == m :
        print(*path)
        return
    
    for i in range(1,n+1):
        if not path :
            path.append(i)
            dfs(depth+1)
            path.pop()
        else :
            if i >= path[-1] :
                path.append(i)
                dfs(depth+1)
                path.pop()
            else :
                continue
dfs(0)