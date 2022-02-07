#   Hailstone 문제
#   숫자 입력 -> 홀수 : 3n + 1 / 짝수 : n / 2 를 반복
#   언젠가는 1이 된다. => 몇 단계만에 1이 되었는가?

#   두 개의 숫자를 입력받아서 두 수 사이의 단계가 제일 많이 걸리는 숫자가 뭔지 + 몇 단계 만에 1이 되는지를 출력

#   ex. 10, 20 => 17이 35단계만에 1이 되어 제일 오래 걸립니다.

start_num = int(input('시작 자연수 하나 입력 : '))
end_num = int(input('종료 자연수 하나 입력 : '))

# 시작 숫자가 더 크다면 변수 값 서로 변경
if start_num > end_num :
    backup = start_num
    start_num = end_num
    end_num = backup

for num in range(start_num, end_num+1) :
    print(num)
    # 각 num에 대한 Haiestone 단계 구하기
    
    count = 0
    
    while True :
        
        if num == 1:
            break
        
        count += 1
        
        for num in range(num) :
            if num % 2 == 1:
                num = num * 3 + 1
                if num == 1 :
                    break    
            else :
                num = num // 2
            
                if num == 1 :
                    break    
        print(num)
    
