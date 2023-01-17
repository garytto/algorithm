numberlength = int(input())
numbers = list(map(int, input().split()))
numberlist = []
for i in range(numberlength):
    numberlist.append(numbers[i])
numberlist.sort()
print(f'{numberlist[0]} {numberlist[numberlength-1]}')
