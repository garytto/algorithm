N , M = map(int,input().split())
numbers = list(map(int,input().split()))
def result(n, m, number):
    n_sum = 0

    for i in range(n-2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                tmp = number[i] + number[j] + number[k]
                if n_sum < tmp <= m:
                    n_sum = tmp
                if n_sum == m:
                    return tmp

    return n_sum
print(result(N, M, numbers))