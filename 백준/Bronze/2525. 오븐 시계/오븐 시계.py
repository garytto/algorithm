h, m = map(int,input().split())
x = int(input())
num = [int(x//60),int(x%60)] # 입력 받은 수를 시와 분으로 나눠 저장.
# 1차 계산
h += num[0] 
m += num[1]
if m >= 60:
    h += 1
    m -= 60
# 24시 이상이거나 0시 미만인 경우를 대응
if h > 23:
    h -= 24
print(f'{h} {m}')