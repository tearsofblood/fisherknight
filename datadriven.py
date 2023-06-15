#This is a CPI forecast illustration to FK's data driven take

import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
import statsmodels.api as sm

# API key from FRED (replace 'YOUR_API_KEY' with your actual API key). You can get it for free if you register at FRED
api_key = 'YOUR_API_KEY'

fred = Fred(api_key=api_key)
cpi_data = fred.get_series('CPIAUCSL', start='1970-01-01')
df = pd.DataFrame({'CPI': cpi_data})
df.index = pd.to_datetime(df.index)

actual_data = df[df.index.year < 2024]
future_data = df[df.index.year >= 2024]

# Split the actual data into features (X) and target (y)
X_actual = sm.add_constant(actual_data.index.to_julian_date())
y_actual = actual_data['CPI']

model = sm.OLS(y_actual, X_actual)
results = model.fit()

future_dates = pd.date_range(start='2024-01-01', end='2029-12-31', freq='M')

future_X = sm.add_constant(future_dates.to_julian_date())

future_predictions = results.predict(future_X)

plt.figure(figsize=(10, 6))
plt.plot(actual_data.index, actual_data['CPI'], label='Actual CPI (Before 2024)')
plt.plot(future_dates, future_predictions, label='Predicted CPI (2024-2029)')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.title('Actual and Predicted CPI')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
