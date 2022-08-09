from grab_data import ohlcv
from datetime import date
  

today = date.today()

dt = ['20220101', str(today)]

data = pd.read_csv('/Users/aronnyberg/Downloads/crypto200 - Sheet1.csv')
#assetList = data.iloc[:,2].values
#assetList = [i for i in assetList][100:120]
assetList = ['RVN','ANKR','ICX','ZEN','LPT','RENBTC','REV','ZIL','SC','NFT','BNT','SUSHI','TEL','AUDIO','BTG','GNO']
  
#NEED TO FIND PAIRS TO GRAB  
  
#['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Exch', 'Pair']
pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume','Exch', 'Pair'])
for each in assetList[:]:
  for base in ['USD', 'GBP', 'EUR', 'JPY', 'ETH']:
    try:
      ticker = each+'/'+base
    except:
      ticker = base+'/'+each
    else:
      print(str(ticker)+"didn't return any data")
    for exch in [binance, ftx, gemini, kraken, bitstamp, bitfinex]:
      try:
        df = ohlcv(exch, dt, 'ETH/BTC', '1m')
      except:
          pass
  time.sleep (exch.rateLimit / 1000)
