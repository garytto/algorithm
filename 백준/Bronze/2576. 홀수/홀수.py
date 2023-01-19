numbers = []
numbers_l = []
cnt = 0
for i in range(7): # 7개의 숫자 입력 받음
    num = int(input())
    numbers.append(num)
for i in range(7):
    if numbers[i]%2 != 0:
        numbers_l.append(numbers[i])
        cnt += 1
if cnt > 0:
    print(sum(numbers_l))
    print(min(numbers_l))
else:
    print(-1)