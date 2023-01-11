a , b = map(int, input().split())
game = True

while game:
    if a == 1 and b == 3:
        print('A')
        break
    elif b == 1 and a == 3:
        print('B')
        break
    elif a < b:
        print('B')
        break
    elif b < a:
        print('A')
        break