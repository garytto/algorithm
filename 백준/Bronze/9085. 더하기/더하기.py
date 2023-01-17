TC = int(input())
for tc in range(1, TC+1):
    numlength = int(input())
    numbers = list(map(int,input().split()))
    numbersum = 0
    for i in range(numlength):
        numbersum += numbers[i]
    print(numbersum)