n = int(input())
cnt = 0
print((2**n)-1)
def hanoi(n,start,end,mid):
    global cnt
    if n == 1 :
        print(start,end)
        return
    
    hanoi(n-1,start,mid,end)
    
    
    print(start,end)
    

    hanoi(n-1,mid,end,start)
    

hanoi(n,1,3,2)
