T = int(input())
for t in range(1, T+1):
    string = input().split()
    for i in range(len(string)):
        string[i] = string[i][::-1]
    print(*string, end = " ")