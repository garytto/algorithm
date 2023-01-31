numbers = []
cnt = 0
result = 0

for i in range(10):
    numbers.append(int(input()))

for i in range(10):
    if cnt < numbers.count(numbers[i]):
        cnt = numbers.count(numbers[i])
        result = numbers[i]

print(sum(numbers)//10)
print(result)