import sys
input = sys.stdin.readline

n = int(input())
blocks = [int(input()) for _ in range(n)]
# print(f'블럭들 :  {blocks}')
max_height = blocks[-1] # 오른쪽에서 보기에 최대 높이는 제일 마지막에 들어가는 값이다.
# print(f'최대 높이 :  {max_height}')
cnt = 1 # 최대 높이 = 맨오른쪽 1개부터 계산.
 
for i in range(n):
    temp = blocks.pop()
    if max_height < temp:
        cnt += 1
        max_height = temp
print(cnt)