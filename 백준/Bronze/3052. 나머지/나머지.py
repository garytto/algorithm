import sys
input = sys.stdin.readline

a = []
for i in range(10):
    array = int(input())
    b = array % 42
    a.append(b)
c = set(a)
print(len(c))