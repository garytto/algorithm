import sys
input = sys.stdin.readline

people = int(input())
people_list = list(map(int,input().split()))

sit = []
sum = 0

for i in range(people):
    if people_list[i] in sit:
        sum += 1
    else:
        sit.append(people_list[i])
print(sum)
