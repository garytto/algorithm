h, m = map(int,input().split())

num = int(m - 45)
if num < 0:
    m = 60 + num
    h -= int(1)
if num >= 60:
    m = int(num - 60)
    h += int(1)
if num >= 0 and num < 60:
    m -= 45
if h < 0:
    h = 23
if h > 23:
    h = 0
print(f'{h} {m}')