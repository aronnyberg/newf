#!/usr/bin/python
import ccxt
import calendar
from datetime import datetime, date, timedelta

binance = ccxt.binance()
#binance.load_markets ()
ftx = ccxt.ftx () 
#ftx.load_markets ()
gemini = ccxt.gemini ()
#gemini.load_markets ()
kraken = ccxt.kraken () 
#kraken.load_markets ()
bitfinex = ccxt.bitfinex ()
#bitfinex.load_markets ()
bitstamp = ccxt.bitstamp () 
#bitstamp.load_markets ()

def min_ohlcv(exch, dt, pair, limit):
    # UTC native object
    since = calendar.timegm(dt.utctimetuple())*1000
    ohlcv1 = exch.fetch_ohlcv(symbol=pair, timeframe='1m', since=since, limit=limit)
    ohlcv2 = exch.fetch_ohlcv(symbol=pair, timeframe='1m', since=since, limit=limit)
    ohlcv = ohlcv1 + ohlcv2
    return ohlcv

def ohlcv(exch, dt, pair, period='1d'):
    ohlcv = []
    limit = 1000
    if period == '1m':
        limit = 720
    elif period == '1d':
        limit = 365
    elif period == '1h':
        limit = 24
    elif period == '5m':
        limit = 288
    for i in dt:
        start_dt = datetime.strptime(i, "%Y%m%d")
        since = calendar.timegm(start_dt.utctimetuple())*1000
        if period == '1m':
            ohlcv.extend(min_ohlcv(exch, start_dt, pair, limit))
        else:
            ohlcv.extend(exch.fetch_ohlcv(symbol=pair, timeframe=period, since=since, limit=limit))
    df = pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Exch', 'Pair'])
    df['Time'] = [datetime.fromtimestamp(float(time)/1000) for time in df['Time']]
    df['Open'] = df['Open'].astype(np.float64)
    df['High'] = df['High'].astype(np.float64)
    df['Low'] = df['Low'].astype(np.float64)
    df['Close'] = df['Close'].astype(np.float64)
    df['Volume'] = df['Volume'].astype(np.float64)
    df['Exch'] = df['Exch'].astype(str)
    df['Pair'] = df['Pair'].astype(str)
    df.set_index('Time', inplace=True)
    return df
