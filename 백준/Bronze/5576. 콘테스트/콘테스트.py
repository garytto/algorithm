import sys
input = sys.stdin.readline

w = []
k = []

for i in range(20):
    if i < 10:
        w.append(int(input()))
    else:
        k.append(int(input()))
w = sorted(w, reverse=True)
k = sorted(k, reverse=True)
w_ans = w[0] + w[1] + w[2]
k_ans = k[0] + k[1] + k[2]
print(w_ans, k_ans)
