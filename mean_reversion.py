def mean_reversion(closes, in_position):
    import talib
    import numpy as np

    BBANDS_PERIOD = 20
    STD_DEV = 2

    if len(closes) > BBANDS_PERIOD:
            closes = np.array(closes)

            upper_band, middle_band, lower_band = talib.BBANDS(closes, timeperiod=BBANDS_PERIOD, nbdevup=STD_DEV, nbdevdn=STD_DEV, matype=talib.MA_Type.SMA)
            
            last_close = closes[-1]
            last_upper_band = upper_band[-1]
            last_middle_band = middle_band[-1]
            last_lower_band = lower_band[-1]
            
            if (last_close <= last_lower_band):
                if in_position:
                    return 'no action'
                else:
                    return 'buy'
                
            if (last_close >= last_upper_band):
                if in_position:
                    return 'sell'
                else:
                    return 'no action'      