number = int(input())
num = number # 비교용과 나누기 위해
cnt = 0
while True:
    a = num //10 
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt += 1
    if num == number:
        break
print(cnt)