from grab_data import ohlcv, find_pairs
from datetime import date
  
today = date.today()

dt = ['20220101', str(today)]

assetList = ['RVN','ANKR','ICX','ZEN','LPT','RENBTC','REV','ZIL','SC','NFT','BNT','SUSHI','TEL','AUDIO','BTG','GNO']
  
#NEED TO FIND PAIRS TO GRAB  


  
#['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Exch', 'Pair']
pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume','Exch', 'Pair'])
for asset in assetList[:]:
  for exch in [binance, ftx, gemini, kraken, bitstamp, bitfinex]:
    for available_pair in find_pairs(exch, asset):
      try:
        df = ohlcv(exch, dt, available_pair, '1m')
      except:
          pass
  time.sleep(exch.rateLimit / 1000)
