def recursion (char,l,r):
    global cnt
    cnt += 1

    if l >= r :
        return 1

    elif char[l] != char[r] :
        return 0
    else :
        return recursion(char,l+1,r-1)
    

def ispalindrome(char):
    return recursion(char,0,len(char)-1)

for tc in range(1,int(input())+1):
    char = input().strip()
    cnt = 0
    print(ispalindrome(char),cnt)