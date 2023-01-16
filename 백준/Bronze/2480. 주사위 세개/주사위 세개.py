numlist = list(map(int, input().split()))
numlist.sort()
result = 0
if numlist[0] == numlist[1] and numlist[1] == numlist[2] and numlist[0] == numlist[2]:
    result = 10000 + (numlist[0] * 1000)
if numlist[0] == numlist[1] and numlist[1] != numlist[2]:
    result = 1000 + (numlist[0] * 100)
if numlist[0] != numlist[1] and numlist[1] == numlist[2]:
    result = 1000 + (numlist[1] * 100)
if numlist[0] != numlist[1] and numlist[1] != numlist[2] and numlist[0] != numlist[2]:
    result =  numlist[2]*100
print(result)