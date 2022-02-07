import random

# 추가 문제 => 코인을 각각 20개씩 갖고 시작
# 홀/짝에 몇 개를 배팅할 지 1~5 사이로 입력 제한
#  => 내가 가진 코인 갯수보다 많이 배팅은 불가
# 배팅한 갯수만큼 코인이 이동하도록

# 추가 문제 2. 게임 룰 변경 0, 1, 2 중에 맞추기
# 랜덤 숫자 -> 0 ~ 2로 범위 변경
# CPU문제 한 번, 내가 문제 한 번씩 번갈아가면서 -> CPU가 맞추기 (랜덤 0~2)
# 몇 개의 코인을 걸지도 입력 1~5개로 (동일하게)

user_coin = 10
cpu_coin = 10

while True:
    
    # 컴퓨터가 0~2개 사이의 구슬을 세팅함
    cpu_count = random.randint(0, 2)
        
    # 셋 중에 하나인지 답을 입력
    
    user_answer = input('0, 1, 2 중 하나만 선택')
    
    if user_answer not in ['0', '1', '2']:
        print('잘못된 입력입니다.')
        continue  # 반복문의 이번 바퀴만 skip
    
    
    # 몇 개의 코인을 배팅할지
    user_bet_coin = int(input('몇 개의 코인을 배팅? 1~5 사이 : '))
    
    if user_bet_coin not in range(1, 6):  # 1~6직전 : 1~5 사이에 없는가?
        print('1~5개 사이만 배팅 가능합니다.')
        continue
    
    if user_bet_coin > user_coin:  # 내가 가진 코인보다 더 많이 배팅함
        print('보유 코인이 부족합니다.')
        continue
    
    if user_bet_coin > cpu_coin:  # CPU가 코인 부족
        print('상대방의 보유 코인이 부족합니다.')
        continue
    
        
    # 제대로 입력했다면 마저 진행
    
    # CPU가 몇 개를 집었는지 공개
    print(f"CPU는 {cpu_count}개의 구슬을 집었습니다.")
    
    if user_answer == '0':
        if cpu_count == '0' :
            
            print('사용자 승리입니다.')
            
            # 사용자 승리 => 코인을 배팅한 만큼 CPU로부터 받아오자
            user_coin += user_bet_coin
            cpu_coin -= user_bet_coin
            
        elif cpu_count == '1' :
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
            
        else:
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
    elif user_answer == '1':
        # 짝을 입력한 경우
        if cpu_count == '1' :
            
            print('사용자 승리입니다.')
            # 맞춘 경우
            user_coin += user_bet_coin
            cpu_coin -= user_bet_coin
            
        elif cpu_count == '0' :
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
            
        else:
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
            
    elif user_answer == '2':
        # 짝을 입력한 경우
        if cpu_count == '2' :
            
            print('사용자 승리입니다.')
            # 맞춘 경우
            user_coin += user_bet_coin
            cpu_coin -= user_bet_coin
            
        elif cpu_count == '0' :
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
            
        else:
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
            
    # 현재 각자의 코인 갯수도 출력
    
    print(f'사용자 보유 코인 : {user_coin}개')
    print(f'CPU 보유 코인 : {cpu_coin}개')
            
    # 둘 중 하나의 코인이 다 떨어졌다면? => 경기 종료
    
    if user_coin == 0:
        print('사용자의 코인이 바닥 났습니다.')
        print('GAME OVER')
        break
    elif cpu_coin == 0:
        print('CPU의 코인이 바닥 났습니다.')
        print('YOU WIN')
        break