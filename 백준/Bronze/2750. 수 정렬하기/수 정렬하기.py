numberlength = int(input())
numbers = []
for i in range(numberlength):
    n = int(input())
    numbers.append(n)
numbers.sort()
for i in range(numberlength):
    print(numbers[i])