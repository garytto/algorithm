test_case = int(input())

for i in range(1, test_case + 1):
    numbers = list(map(int, input().split()))
    numbersum = int(sum(numbers)) # 차마 합계까지 for 문돌리기 귀찮아서..
    avg = numbersum//int(len(numbers)) # 평균 구하기
    numberleft = numbersum % int(len(numbers)) # 나머지 값 여부 확인용
    if numberleft > 0: # 나머지 값이 있다면
        countleft = int((numberleft/len(numbers)) * 10) # 계산하기 편하기 위해 소숫점 1자리 값만 올리기
        if countleft > 5: # 소숫 점 1자리에 있는 값이 5보다 높다면... 추가한다 의 계산식 만든것
            avg += 1
    print(f'#{i} {avg}')
