import sys
input = sys.stdin.readline

string = input().rstrip()
for i in range(0, len(string), 10):
    endline = i + 10 # 10개씩 끊어서 출력하니 해당 부분에 대응
    # print(i) # 정상적으로 순서에 맞춰 진행되는지 확인. 위에 range(0, len(string), 10) <- i가 10씩 되는지 확인
    print(string[i:endline])