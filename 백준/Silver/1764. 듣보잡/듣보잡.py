import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}
answer = []
for _ in range(m+n):
    s = input().rstrip()
    if s in dic:
        answer.append(s)
    else:
        dic.setdefault(s)

print(len(answer))
answer = sorted(answer)

for i in answer:
    print(i)