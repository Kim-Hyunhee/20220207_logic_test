# requests 라이브러리 활용 -> API 연계

# 한국 BTC 시세 VS 해외 BTC 시세 비교
import requests

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
        
print(f'해외 Binance의 BTC 가격 : {binance_btc_price_dollar}')