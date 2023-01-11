
number = int(input())
numbers = []
for i in range(number+1): # 숫자 넣기
    numbers.append(i)

numberssum = sum(numbers) # 숫자 합계 구하기
print(numberssum)