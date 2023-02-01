TC = int(input())
for i in range(TC):
    number_list = list(map(int, input().split()))
    number_sort = sorted(number_list)
    number_sort.pop(0)
    number_sort.pop(3)
    num_gap = number_sort[2] - number_sort[0]

    if num_gap >= 4:
        print('KIN')
    else:
        print(sum(number_sort))