import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    string = input().rstrip().split()
    for i in range(len(string)):
        string[i] = string[i][::-1]
    print(*string, end = " ")