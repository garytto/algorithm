numcnt = int(input())

for i in range(numcnt):
    num = list(input())
    for j in range(len(num)-1):
        if num[j]==num[j + 1]: 
            pass
        
        elif num[j] in num[j + 2:]:
            numcnt -= 1
            break
print(numcnt)