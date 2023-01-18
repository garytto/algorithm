string = input().rstrip()
sList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in sList:
    string = string.replace(i, "@")
print(len(string))