import pandas as pd

# Set the FRED API key
api_key = 'your_api_key'

# Set the dates and the variable
series_id = 'GDP'
observation_start = '2020-01-01'
observation_end = '2020-12-31'

url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&observation_start={observation_start}&observation_end={observation_end}&api_key={api_key}'
df = pd.read_json(url)
df.to_csv('fred_data.csv')
