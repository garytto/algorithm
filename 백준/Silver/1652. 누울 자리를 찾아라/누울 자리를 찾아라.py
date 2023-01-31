numbers = int(input())
array = [input()+'X' for _ in range(numbers)] + ['X' *(numbers+1)]

def check_r():
    result = 0
    for i in range(numbers):
        cnt = 0
        for j in range(numbers+1):
            if array[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
    return result

def check_col():
    result = 0
    for j in range(numbers):
        cnt = 0
        for i in range(numbers+1):
            if array[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
    return result
    
print(check_r(), check_col())