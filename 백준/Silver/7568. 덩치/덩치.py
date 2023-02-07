import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
rank = [1 for _ in range(n)]
# print(rank)

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    rank[i] += cnt
    
print(*rank)