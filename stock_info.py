import yfinance as yf

stock1=yf.Ticker("BABA")
stock1_info=stock1.info
print(stock1_info)