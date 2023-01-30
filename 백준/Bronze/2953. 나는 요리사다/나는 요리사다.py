list_list = []
mNum = 0
index = 0
for i in range(5): # 5줄
    list_list.append(list(map(int, input().split()))) # 리스트로 값 저장
    if mNum < sum(list_list[i]):
        index = i + 1 # i는 0 부터시작 순서는 1부터 시작
        mNum = sum(list_list[i])
print(index, mNum)