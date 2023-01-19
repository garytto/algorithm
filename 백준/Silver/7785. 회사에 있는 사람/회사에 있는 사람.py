import sys
input = sys.stdin.readline

N = int(input())
person = {}
for n in range(N):
    a, b = input().rstrip().split()
    if a not in person:
        person[a] = b
    elif a in person:
        if b == 'leave':
            del(person[a])

personlist = sorted(person, reverse=True)
for i in personlist:
    print(i)
