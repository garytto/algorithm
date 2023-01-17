numberlength = int(input())
numbers = list(map(int, input()))
numberlist = []
for i in range(numberlength):
    numberlist.append(numbers[i])
print(sum(numberlist))
