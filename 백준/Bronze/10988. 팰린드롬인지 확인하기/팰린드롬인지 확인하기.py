import sys

input = sys.stdin.readline

string = input().rstrip()
if string == string[::-1]:
    print('1')
else:
    print('0')