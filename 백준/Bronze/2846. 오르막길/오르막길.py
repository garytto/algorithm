import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# result = [] # 아래식이 더 좋으므로 폐기
# for _ in range(n):
#     result.append(0) 

result = [0]*n
# print(result)
for i in range(n):
    cnt = 0
    for j in range(i+1, n):
        if numbers[j] > numbers[j-1]:
            tmp = numbers[j] - numbers[j-1]
            cnt += tmp
        else:
            break
    result[i] = cnt
print(max(result))