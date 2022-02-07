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
    print('홀/짝 판별 차례')
    