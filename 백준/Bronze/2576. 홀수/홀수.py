numbers = []
cnt = 0
for i in range(7): # 7개의 숫자 입력 받음
    num = int(input())
    if num%2 != 0:
        numbers.append(num)
        cnt += 1

if cnt > 0:
    print(sum(numbers))
    print(min(numbers))
else:
    print(-1)
