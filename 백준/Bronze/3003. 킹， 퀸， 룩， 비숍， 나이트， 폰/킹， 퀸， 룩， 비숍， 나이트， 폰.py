black = list(map(int, input().split()))
white = [1, 1, 2, 2, 2, 8]
for i in range(len(black)):
    black[i] = white[i] - black[i]
for i in black:
    print(i,end=' ')