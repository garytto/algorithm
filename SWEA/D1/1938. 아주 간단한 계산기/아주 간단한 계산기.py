a, b = list(map(int,input().split()))

for i in [a + b, a - b, a * b, a // b]:
    print(f'{i}')