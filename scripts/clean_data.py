import pandas as pd
import os

df = pd.read_csv('data/raw/gdp_korea.csv')
df['GDP YoY Change (%)'] = df['GDP (Billion USD)'].pct_change() * 100

os.makedirs('dashboard', exist_ok=True)
df.to_excel('dashboard/tableau_data.xlsx', index=False)
