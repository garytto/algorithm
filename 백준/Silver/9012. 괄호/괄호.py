T = int(input())
for i in range(T) :
    array = list(input())
    answer = 0
    for j in array :
        if j == "(" :
            answer += 1
        elif j == ")" :
            answer -= 1
        if answer < 0 :
            print('NO')
            break
    if answer == 0 :
        print('YES')
    elif answer > 0 :
        print('NO')    