test_case = int(input())

for i in range(1, test_case + 1):
    a, b = list(map(int,input().split()))
    print(f'#{i} {a//b} {a%b}')