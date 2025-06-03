import pandas as pd
import datetime
import os

# Simulate GDP data for South Korea (fake data for now)
years = list(range(2015, datetime.datetime.now().year + 1))
gdp_values = [1600 + i * 100 for i in range(len(years))]

df = pd.DataFrame({
    'Year': years,
    'GDP (Billion USD)': gdp_values
})

# Save to CSV
os.makedirs('data/raw', exist_ok=True)
df.to_csv('data/raw/gdp_korea.csv', index=False)
