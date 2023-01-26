import sys
input = sys.stdin.readline

number = int(input())
list = []
for i in range(number):
    num = int(input())
    if num == 0:
        list.pop()
    else:
        list.append(num)

print(sum(list))