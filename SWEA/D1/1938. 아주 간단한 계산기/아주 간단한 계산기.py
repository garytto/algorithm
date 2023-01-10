a, b = list(map(int,input().split()))

cal2 = [a + b, a - b, a * b, a // b]

for i in range(len(cal2)):
    print(f'{cal2[i]}')