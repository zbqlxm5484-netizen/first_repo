import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(input().strip()) for _ in range(n)]

# 적록색약 보드 (R -> G)
cb = [row[:] for row in board]
for i in range(n):
    for j in range(n):
        if cb[i][j] == 'R':
            cb[i][j] = 'G'

dirs = ((1,0), (-1,0), (0,1), (0,-1))

def count_regions(g):
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            color = g[i][j]
            stack = [(i, j)]
            visited[i][j] = True
            cnt += 1

            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if not visited[nr][nc] and g[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
    return cnt

print(count_regions(board), count_regions(cb))