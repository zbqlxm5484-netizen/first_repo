T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = 0
    j = 0
    result = []

    while i < N or j < M :
        if i < N :
            result.append(a[i])
            i += 1
        if j < M :
            result.append(b[j])
            j += 1    
    
    print(f"#{tc}", *result)