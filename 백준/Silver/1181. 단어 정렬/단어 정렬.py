import sys
input = sys.stdin.readline

n = int(input())
ls = []

for i in range(n):
    ls.append(input().strip())
s = set(ls)
ls = list(s)

ls.sort()
ls.sort(key=len)

for i in ls:
    print(i)