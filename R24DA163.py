# Develop a system to analyze stock market or financial transaction datasets

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading CSV file
data = pd.read_csv("stock_data.csv")

# Display dataset
print("----- STOCK MARKET DATASET -----")
print(data)

# Statistical Analysis
mean_close = np.mean(data['Close'])
median_close = np.median(data['Close'])
std_close = np.std(data['Close'])

print("\n----- STATISTICAL ANALYSIS -----")
print("Mean Closing Price :", mean_close)
print("Median Closing Price :", median_close)
print("Standard Deviation :", std_close)

# Maximum and Minimum Closing Price
print("\nMaximum Closing Price :", data['Close'].max())
print("Minimum Closing Price :", data['Close'].min())

# Profit/Loss Calculation
data['Profit/Loss'] = data['Close'] - data['Open']

print("\n----- PROFIT / LOSS ANALYSIS -----")
print(data[['Date', 'Open', 'Close', 'Profit/Loss']])

# Total Volume
total_volume = np.sum(data['Volume'])
print("\nTotal Trading Volume :", total_volume)

# Graph Visualization
plt.figure(figsize=(8,5))

plt.plot(data['Date'], data['Close'], marker='o')

plt.title("Stock Market Analysis")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.xticks(rotation=45)
plt.grid(True)

plt.show()