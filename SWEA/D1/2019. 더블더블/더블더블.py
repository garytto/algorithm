number = int(input())
numberlist = []
for i in range(number+1):
    cal = 1 * (2**i)
    numberlist.append(cal)
print(*numberlist)