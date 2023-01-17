a_1, a_2 = map(int,input().split())
b_1, b_2 = map(int,input().split())
c_1, c_2 = map(int,input().split())

def define(a, b, c):
    if a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b

d_1 = define(a_1, b_1, c_1)
d_2 = define(a_2, b_2, c_2)
print(d_1, d_2)