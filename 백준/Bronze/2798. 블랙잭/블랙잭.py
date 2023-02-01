N , M = map(int,input().split())
numbers = list(map(int,input().split()))
n_sum = 0
end = 0

for i in range(N-2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = numbers[i] + numbers[j] + numbers[k]
            if n_sum < tmp <= M:
                n_sum = tmp
print(n_sum)