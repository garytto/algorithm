import sys
input = sys.stdin.readline
number = int(input())

while True:
    if len(str(number)) == str(number).count('4') + str(number).count('7'): # 4또는 7이 도합해서 number의 자릿수 까지만 있기 때문에 접근
        print(number)
        break
    number -= 1
