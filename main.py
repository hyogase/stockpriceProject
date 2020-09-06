import yfinance as yf
import matplotlib.pyplot as plt

stock1=yf.Ticker("BABA")
hist=stock1.history(peroid="max")
hist_close=hist['Close']
plt.figure(figsize=(26,14))
plt.title('BABA')
hist_close.plot()
plt.savefig('BABA.png')
plt.show()