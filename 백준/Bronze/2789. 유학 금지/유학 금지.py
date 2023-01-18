import sys
input = sys.stdin.readline

string = input().rstrip()
for i in 'CAMBRIDGE':
    if i in string:
        string = string.replace(i, "")
print(string)