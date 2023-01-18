a, b = input().rstrip().split('(^0^)') # 얼굴을 기점으로 하여 a, b 를 나누어 저장(왼 오른)
A = a.count('@') # 주먹의 잔상을 구하는 문제이기에 주먹의 갯수만 세기
B = b.count('@')
print(A, B)