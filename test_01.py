#   Hailstone 문제
#   숫자 입력 -> 홀수 : 3n + 1 / 짝수 : n / 2 를 반복
#   언젠가는 1이 된다. => 몇 단계만에 1이 되었는가?

input_num = int(input('자연수 하나 입력 : '))

count = 0

while True :
    
    if input_num == 1:
        break
    
    count += 1
    
    if input_num % 2 == 1 :
        input_num = input_num * 3 + 1
    else :
        input_num = input_num // 2
        
    print(f"{count}단계 : {input_num}")
    
print(f"{count} 단계만에 1이 되었습니다.")
    
