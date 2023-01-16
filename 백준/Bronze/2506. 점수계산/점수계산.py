numbers = int(input())
cnt = 0
numsum = 0
a = list(map(int,input().split()))

for i in range(0, numbers):
    if a[i] == 1:
        numsum += (1 + cnt)
        cnt += 1
    if a[i] == 0:
        cnt = 0
print(numsum)