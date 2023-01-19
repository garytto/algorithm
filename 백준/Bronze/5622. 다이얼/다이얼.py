import sys
input = sys.stdin.readline

n = input().rstrip()
numbers = {'ABC': int(3), 'DEF': int(4),'GHI': int(5),'JKL': int(6),'MNO': int(7),'PQRS': int(8),'TUV': int(9),'WXYZ': int(10)}
result = 0
for i in numbers.keys(): ## key값을 i로 받아옴.
    for j in n: # 입력받은 n을 하나 하나 j에게 받아옴
        if j in i: # keys에서 받은 i의 값에 j가 들어가있다면.
            result += numbers[i] # 관련 키의 value 값을 result에 넣어준다.
        else:
            pass
print(result)