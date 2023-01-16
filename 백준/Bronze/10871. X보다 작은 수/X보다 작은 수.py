cnt, Mnum = map(int, input().split())
numlist = list(map(int, input().split()))
for i in range(cnt):
    if numlist[i] < Mnum:
        print(numlist[i], end=" ")