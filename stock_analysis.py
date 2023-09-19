import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and date range
stock_symbol = "RELIANCE.BO"  # Reliance Industries Limited on BSE
start_date = "2022-01-01"
end_date = "2023-09-12"

# Fetch historical data
df = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns
df['Daily_Return'] = df['Adj Close'].pct_change()

# Plot the closing price
plt.figure(figsize=(12, 6))
plt.title(f'{stock_symbol} Closing Price')
plt.plot(df.index, df['Adj Close'], label='Closing Price')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid()
plt.show()

# Plot daily returns
plt.figure(figsize=(12, 6))
plt.title(f'{stock_symbol} Daily Returns')
plt.plot(df.index, df['Daily_Return'], label='Daily Returns', color='green')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.grid()
plt.show()
