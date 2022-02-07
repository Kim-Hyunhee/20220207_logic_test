# requests 라이브러리 활용 -> API 연계

# 한국 BTC 시세 VS 해외 BTC 시세 비교
from time import sleep
import requests
import datetime

while True:
    # 자동 모니터링 진행
    print(f'현재 일시 : {datetime.datetime.now()}')

    # 업비트의 현대 시세 조회 API 호출
    upbit_response = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-BTC')

    upbit_response_json = upbit_response.json()

    upbit_btc_price = upbit_response_json[0]['trade_price']

    print(f'국내 Upbit의 BTC 가격 : {upbit_btc_price}원')

    # 바이낸스의 현재 시세 조회 -> $로 리턴됨 * 환율로 원화로 만들어서 업비트와 비교

    binance_response = requests.get('https://api.binance.com/api/v1/ticker/allPrices')
    binance_json = binance_response.json()

    # binance_json은 일종의 리스트

    for coin_item in binance_json:
        if coin_item['symbol'] == 'BTCUSDT' :
            binance_btc_price_dollar = float(coin_item['price'])
            
    print(f'해외 Binance의 BTC 가격 : {binance_btc_price_dollar}$')


    # 현재 1달러 당 원화로는 얼마인지? -> API 활용

    dollar_response = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD')
    dollar_json = dollar_response.json()

    dollar_won = dollar_json[0]['basePrice']

    print(f'현재 환율 : {dollar_won}')

    binance_btc_price_won = binance_btc_price_dollar * dollar_won
    print(f'해외 Binance의 BTC 가격 : {binance_btc_price_won}원')


    # 프리미엄이 몇 % 붙어있는가?
    premium = (upbit_btc_price - binance_btc_price_won) / binance_btc_price_won * 100

    # 소수점 2자리까지 표기
    premium = round(premium, 2)

    print(f'국내 BTC가 해외 BTC보다 {premium}% 더 비쌉니다.')
    
    # 2초 정지 -> 재실행
    sleep(2)