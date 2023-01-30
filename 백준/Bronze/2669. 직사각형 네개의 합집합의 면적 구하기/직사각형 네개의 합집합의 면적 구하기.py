import sys
input = sys.stdin.readline

board = [[0 for _ in range(101)] for _ in range(101)] # 공간 좌표 생성.
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1 # 보드에 색칠하기. += 쓰면 안됨. 중복 되는 경우에는 그저 1로 해둬서 중복인 경우 의미 없는 행동을 하기 위해 1로 "바꾼다"의 개념으로 = 사용.

for n in board:
    result += sum(n) # board에 색칠 되어 있는 아이들 합 더하기.(1로 지정해둔 아이들.)
print(result)
