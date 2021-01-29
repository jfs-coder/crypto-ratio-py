# import the request library
import requests

TICKER_API_URL = 'https://api.bitfinex.com/v1/pubticker/'

def get_price(crypto):
	response = requests.get(TICKER_API_URL+crypto)
	response_json = response.json()

	return float(response_json['last_price'])

# randomly chosen coins to test with.

ETHUSD = get_price('ethusd')
DOTUSD = get_price('dotusd')
ADAUSD = get_price('adausd')
IOTUSD = get_price('iotusd')
LTCUSD = get_price('ltcusd')

print(f'\nETHUSD: {ETHUSD}\nDOTUSD: {DOTUSD}\nADAUSD: {ADAUSD}\nIOTUSD: {IOTUSD}\nLTCUSD: {LTCUSD}\n')

# here we will create all the ratios

print(f'ETH / DOT: {ETHUSD/DOTUSD}\n')
print(f'ETH / ADA: {ETHUSD/ADAUSD}\n')
print(f'ETH / IOT: {ETHUSD/IOTUSD}\n\n')

print(f'DOT / ADA: {DOTUSD/ADAUSD}\n')
print(f'DOT / IOT: {DOTUSD/IOTUSD}\n')
print(f'DOT / ETH: {DOTUSD/ETHUSD}\n\n')

print(f'ADA / IOT: {ADAUSD/IOTUSD}\n')
print(f'ADA / ETH: {ADAUSD/ETHUSD}\n')
print(f'ADA / DOT: {ADAUSD/DOTUSD}\n\n')

print(f'IOT / ETH: {IOTUSD/ETHUSD}\n')
print(f'IOT / DOT: {IOTUSD/DOTUSD}\n')
print(f'IOT / ADA: {IOTUSD/ADAUSD}\n\n')




