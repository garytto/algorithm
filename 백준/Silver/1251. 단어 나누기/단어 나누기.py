import sys
input = sys.stdin.readline

s = input().rstrip()
answer_list = []
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            answer = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            answer_list.append(answer)
answer_list = sorted(answer_list)
print(answer_list[0])
