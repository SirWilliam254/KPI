import numpy as np
import pandas as pd

# Define variables
num_customers = 1000
num_products = 100
min_price = 100
max_price = 4000
profit_margin_min = 0.05
profit_margin_max = 0.17
years = 5
num_data_points = 1000000

# Define function to generate random profits
def get_random_profit():
    return np.random.uniform(profit_margin_min, profit_margin_max)

# Define function to generate sales data
def generate_sales_data():
    data = []
    for i in range(num_data_points):
        # Generate random data
        customer_id = np.random.randint(1, num_customers+1)
        product_id = np.random.randint(1, num_products+1)
        price = np.random.randint(min_price, max_price+1)
        quantity = np.random.randint(1, 7)
        rating = np.random.randint(1, 5)
        origin_country = np.random.choice(['USA', 'China', 'India', 'Japan', 'Germany'])
        # Calculate cost and profit
        cost = price * (1 - get_random_profit())
        profit = price - cost
        # Append to data
        data.append([i+1, customer_id, product_id, price, quantity, rating, origin_country, cost, profit])
    return pd.DataFrame(data, columns=['Sale ID', 'Customer ID', 'Product ID', 'Price', 'Quantity', 'Rating', 'Origin Country', 'Cost', 'Profit'])

# Generate sales data
sales_data = generate_sales_data()

# Save data to CSV file
sales_data.to_csv('sales_data.csv', index=False)
