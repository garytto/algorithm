people_cnt = []
people = 0 

for _ in range(4) :
    people_out, people_in = map(int,input().split())
    people += people_in
    people -= people_out

    people_cnt.append(people) #종착역 마다의 사람 수 추가
    
print(max(people_cnt))