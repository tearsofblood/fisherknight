# This is the demonstration of F(requency) Screen(er), a script that gets quotes from Yahoo Finance,
# analyzes spykes from local lows, and saves the results in csv files locally.
# Made for the June 2023 presentation at Fisher Knight. Ask GGP for the complete version.

import yfinance as yf
import pandas as pd
import numpy as np

ticker_symbol = input("Enter the ticker: ")

start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Getting the data from Yahoo Finance
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

local_lows = pd.DataFrame(columns=["Timestamp", "Low"])

# Iterate through the quotes
for index, row in stock_data.iterrows():
    calculated_low = min(row["Low"], row["Close"])

    # Check if the calculated low is indeed the low we are looking for
    if local_lows.empty or calculated_low < local_lows["Low"].min():
        new_row = pd.DataFrame({"Timestamp": [index], "Low": [calculated_low]})
        local_lows = pd.concat([local_lows, new_row], ignore_index=True)

stock_data["Local_Low"] = np.nan
for index, row in local_lows.iterrows():
    timestamp = row["Timestamp"]
    low = row["Low"]
    stock_data.loc[timestamp, "Local_Low"] = low

# Replacing 'NA'
stock_data["Local_Low"].fillna(method="ffill", inplace=True)

stock_data["Percentage_Difference"] = (stock_data["High"] - stock_data["Local_Low"].shift(1)) / stock_data["Local_Low"].shift(1) * 100

# The intervals are hardcoded because of Alex.
conditions = [
    (stock_data["Percentage_Difference"] <= 0),
    (stock_data["Percentage_Difference"] > 0) & (stock_data["Percentage_Difference"] <= 10),
    (stock_data["Percentage_Difference"] > 10) & (stock_data["Percentage_Difference"] <= 20),
    (stock_data["Percentage_Difference"] > 20) & (stock_data["Percentage_Difference"] <= 25),
    (stock_data["Percentage_Difference"] > 25) & (stock_data["Percentage_Difference"] <= 50),
    (stock_data["Percentage_Difference"] > 50) & (stock_data["Percentage_Difference"] <= 100),
    (stock_data["Percentage_Difference"] > 100) & (stock_data["Percentage_Difference"] <= 200),
    (stock_data["Percentage_Difference"] > 200) & (stock_data["Percentage_Difference"] <= 300),
    (stock_data["Percentage_Difference"] > 300) & (stock_data["Percentage_Difference"] <= 400),
    (stock_data["Percentage_Difference"] > 400)
]

choices = [
    "0", "0+", "10+", "20+", "25+", "50+", "100+", "200+", "300+", "400+"
]

stock_data["spike_type"] = np.select(conditions, choices)

stock_data.to_csv(ticker_symbol+'.csv', index=True)

# Uncomment for intermediate verification
# local_lows.to_csv("local_lows.csv", index=False)

print(stock_data)


