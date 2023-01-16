allprice = int(input()) # 총 가격
buy = int(input()) # 산 물품들
buysum = 0 # 산 물품의 합계를 저장할 곳
for i in range(buy): # 계산
    a, b = map(int, input().split()) 
    buysum += (a * b)
if allprice == buysum: # 비교
    print('Yes')
if allprice != buysum: # 비교
    print('No')