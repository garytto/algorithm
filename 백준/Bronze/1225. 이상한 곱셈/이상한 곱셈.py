import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
c = []
d = []

for i in range(len(a)):
    c.append(int(a[i]))
for i in range(len(b)):
    d.append(int(b[i]))
    
print(sum(c)*sum(d))