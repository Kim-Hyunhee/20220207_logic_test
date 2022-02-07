import random

user_coin = 3
cpu_coin = 3

while True:
    
    # 컴퓨터가 1~6개 사이의 구슬을 세팅함
    cpu_count = random.randint(1, 6)
    
    # 홀 / 짝인지 답을 입력
    
    user_answer = input('홀 / 짝을 맞춰주세요.')
    
    if user_answer not in ['홀', '짝']:
        print('잘못된 입력입니다.')
        continue  # 반복문의 이번 바퀴만 skip
        
    # 제대로 입력했다면 마저 진행
    
    # CPU가 몇 개를 집었는지 공개
    print(f"CPU는 {cpu_count}개의 구슬을 집었습니다.")
    
    if user_answer == '홀':
        if cpu_count % 2 == 1 :
            
            print('사용자 승리입니다.')
            
            # 사용자 승리 => 코인 한 개 CPU로부터 받아오자
            user_coin += 1
            cpu_coin -= 1
        else:
            print('사용자 패배입니다.')
            user_coin -= 1
            cpu_coin += 1
    else:
        # 짝을 입력한 경우
        if cpu_count % 2 == 0 :
            
            print('사용자 승리입니다.')
            # 맞춘 경우
            user_coin += 1
            cpu_coin -= 1
        else:
            
            print('사용자 패배입니다.')
            user_coin -= 1
            cpu_coin += 1