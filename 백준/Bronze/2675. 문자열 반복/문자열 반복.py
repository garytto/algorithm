import sys
input = sys.stdin.readline
TC = int(input())

for tc in range(1, TC+1): # 편의를 위해 0부터 시작하는게 아닌 1로 시작. 첫번째 두번째 세번째.... 로 생각하기 편하게 하기 위해
    num, string = input().rstrip().split()
    result = ''
    num = int(num)
    for i in string:
        result += i*num
    print(result)
