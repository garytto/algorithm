A = int(input())
B = int(input())
C = int(input())
numbersum = str(A*B*C)
number = {}
for i in range(10):
    n = str(i)
    number[n] = 0

for i in numbersum:
    if i in number:
        number[i] += 1
for i in number:
    print(number[i])

