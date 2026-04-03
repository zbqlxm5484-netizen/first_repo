T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tri = []

    for i in range(N) :
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(row)

    print(f"#{tc}")
    for row in tri:
        print(*row)
