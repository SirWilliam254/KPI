import random
import pandas as pd

# Generate random data
data = {'date': pd.date_range(start='2023-01-01', end='2025-12-31', freq='D')}
for kpi in ['revenue', 'profit', 'expenses', 'sales_volume']:
    data[kpi] = [random.uniform(10000, 100000) for _ in range(len(data['date']))]
df = pd.DataFrame(data)

# Calculate KPIs
df['gross_profit_margin'] = (df['revenue'] - df['expenses']) / df['revenue']
df['profit_margin'] = df['profit'] / df['revenue']
df['average_sale_price'] = df['revenue'] / df['sales_volume']
df['sales_growth_rate'] = df['sales_volume'].pct_change()
