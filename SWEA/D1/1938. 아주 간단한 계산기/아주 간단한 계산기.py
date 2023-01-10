a, b = list(map(int,input().split()))

cal = []
numbersum = int(a + b)
numberminus = int(a - b)
numbermulti = int(a * b) # 곱하기는 영어로 multiplication
numberdivision = int(a // b) # 나누기는 영어로 division
cal.append(numbersum)
cal.append(numberminus)
cal.append(numbermulti)
cal.append(numberdivision)

for i in range(len(cal)):
    print(f'{cal[i]}')