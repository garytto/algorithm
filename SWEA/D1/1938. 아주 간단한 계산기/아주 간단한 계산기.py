a, b = list(map(int,input().split()))

calculate = [a + b, a - b, a * b, a // b]

for i in range(len(calculate)):
    print(f'{calculate[i]}')