import sys
input = sys.stdin.readline

string = input().rstrip()
if string.count(":-)") == 0 and string.count(":-(") == 0:
    print("none")
elif string.count(":-)") == string.count(":-("):
    print("unsure")
elif string.count(":-)") > string.count(":-("):
    print("happy")
else:
    print("sad")