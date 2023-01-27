import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(a + b + c - max(a, b, c) - min(a, b, c))