test_case = int(input())

for i in range(1, test_case + 1):
    numbers = list(map(int,input().split()))
    numbers.sort()
    print(f'#{i} {numbers[len(numbers)-1]}')
