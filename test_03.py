# requests 라이브러리 활용 -> API 연계

# 한국 BTC 시세 VS 해외 BTC 시세 비교
import requests

# 업비트의 현대 시세 조회 API 호출
upbit_response = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-BTC')

upbit_response_json = upbit_response.json()

upbit_btc_price = upbit_response_json[0]['trade_price']

print(f'국내 Upbit의 BTC 가격 : {upbit_btc_price}원')