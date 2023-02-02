cup = [0, 1, 0, 0]

for _ in range(int(input())):
    X, Y = map(int, input().split())
    temp =  cup[X]
    cup[X] = cup[Y]
    cup[Y] = temp
    
print(cup.index(1))