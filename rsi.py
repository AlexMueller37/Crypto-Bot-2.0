def rsi(closes, in_position):
    import talib
    import numpy as np 

    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 80 
    RSI_OVERSOLD = 20

    if len(closes) > RSI_PERIOD:
            np_closes = np.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            last_rsi = rsi[-1]
            
            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    return 'sell'
                else: 
                    return 'no action'
                
            if last_rsi < RSI_OVERSOLD:
                if in_position: 
                    return 'no action'
                else: 
                    return 'buy'