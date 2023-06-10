# Symmetric Projection (Mirror Image) Analysis illustration. More information here: https://fisherknight.com/on-symmetric-projection-a-k-a-mirror-image-analysis/

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

ticker = "^VIX"

vix_data = yf.download(ticker, start="2005-01-01", end="2023-12-31")

reflected_data = vix_data[::-1].copy()

# Generate future dates till 2030s
start_date = vix_data.index[-1] + pd.DateOffset(days=1)
end_date = pd.Timestamp("2035-12-31")
future_dates = pd.date_range(start=start_date, end=end_date, freq="B")

projected_data = pd.DataFrame(index=future_dates, columns=vix_data.columns)

# Reflect the historical data into the future
reflected_data = reflected_data[:len(future_dates)]
projected_data.loc[:vix_data.index[-1]] = vix_data
projected_data.loc[vix_data.index[-1]+pd.DateOffset(days=1):] = reflected_data.values

# Plotting the chart
plt.figure(figsize=(10, 6))
plt.plot(vix_data.index, vix_data["Close"], color="red", label="Historical Data")
plt.plot(projected_data.index, projected_data["Close"], color="gray", label="Projected Data")
plt.xlabel("Date")
plt.ylabel("VIX")
plt.title("VIX Historical Data with Projected Reflection")
plt.grid(True)
plt.legend()
plt.gca().set_facecolor("white")
plt.show()
