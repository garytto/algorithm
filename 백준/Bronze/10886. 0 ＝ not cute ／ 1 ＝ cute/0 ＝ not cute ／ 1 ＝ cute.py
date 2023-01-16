Tp = int(input())
result = []
for i in range(1, Tp + 1):
    tmp = int(input())
    result.append(tmp)
cal = [0, 0]
for i in range(int(len(result))):
    if result[i] == int(0):
        cal[0] += 1
    if result[i] == int(1):
        cal[1] += 1
if cal[0] > cal[1]:
    print("Junhee is not cute!")
if cal[0] < cal[1]:
    print("Junhee is cute!")
