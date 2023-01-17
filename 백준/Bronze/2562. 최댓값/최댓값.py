numbers = []
for i in range(9):
    numbers.append(int(input()))
mNum = max(numbers)
for i in range(len(numbers)):
    if numbers[i] == mNum:
        print(mNum)
        print(i+1) # i로 출력 시 인덱스 값인 7만 출력됨. 우리가 원하는건 순서임. 그러므로 +!