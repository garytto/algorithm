import sys
input = sys.stdin.readline

N = int(input())
Numbers = list(map(int,input().split()))
FNumber = int(input())
cnt = 0
for i in range(len(Numbers)):
    if Numbers[i] == FNumber:
        cnt += 1
print(cnt)