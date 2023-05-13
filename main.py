from make_order import order
from mean_reversion import mean_reversion
from rsi import rsi

import numpy as np 
import requests
from time import sleep
from datetime import datetime
import talib

TRADE_SYMBOL = 'BTCUSD'

url = f'https://api.binance.us/api/v3/ticker?symbol={TRADE_SYMBOL}'

closes = []
in_position = False

TRADE_QUANTITY = 1

API_KEY = 'PKEACEMDMC69HGLPAKU0'
SECRET_KEY = 'SdWuBij5goM1FacHxGBVZPgfObz3X4lg2n0F5Evl'

while True: 
    response = requests.get(url)
    response = response.json()

    close = response['lastPrice']
    closes.append(float(close))

    last_price = closes[-1]

    print(f'candle closed at {close}')

    output_mean_reversion = mean_reversion(closes, in_position)
    output_rsi = rsi(closes, in_position)

    if output_mean_reversion == 'buy' and output_rsi == 'buy': 
        print('Buying...')
        order(TRADE_SYMBOL, TRADE_QUANTITY, 'buy', 'market', 'gtc', API_KEY, SECRET_KEY)
        buy_price = last_price
        print('Success!')
        in_position = True
    if output_mean_reversion == 'sell' and output_rsi == 'sell': 
        print('Selling...')
        order(TRADE_SYMBOL, ((TRADE_QUANTITY - (TRADE_QUANTITY * 0.0025)) - 0.000000001), 'sell', 'market', 'gtc', API_KEY, SECRET_KEY)
        sell_price = last_price
        print('Success!')
        in_position = False
    if output_mean_reversion == 'no action' or output_rsi == 'no action': 
        print('No Action Needed')

    print(f'Currently Holding : {in_position}')

    print('===============================================================================================================')
        
    sleep(5)