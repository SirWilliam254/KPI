import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set the number of customers and products
num_customers = 1000
num_products = 100

# Set the date range for the data
start_date = datetime(2017, 1, 1)
end_date = datetime(2021, 12, 31)
num_days = (end_date - start_date).days

# Set the price range for the products
min_price = 100
max_price = 4000

# Generate customer data
customers = pd.DataFrame({
    'customer_id': [i+1 for i in range(num_customers)],
    'country': np.random.choice(['USA', 'UK', 'Canada', 'Australia', 'Germany'], num_customers),
})

# Generate product data
products = pd.DataFrame({
    'product_id': [i+1 for i in range(num_products)],
    'product_price': np.random.randint(min_price, max_price+1, num_products),
    'product_origin': np.random.choice(['USA', 'UK', 'China', 'Italy', 'Mexico'], num_products),
})

# Generate sales data
sales = pd.DataFrame()
for i in range(num_days):
    date = start_date + timedelta(days=i)
    num_sales = np.random.randint(0, 10)
    if num_sales > 0:
        customer_ids = np.random.choice(customers['customer_id'], num_sales)
        product_ids = np.random.choice(products['product_id'], num_sales)
        product_prices = products.loc[products['product_id'].isin(product_ids), 'product_price'].tolist()
        product_origins = products.loc[products['product_id'].isin(product_ids), 'product_origin'].tolist()
        sale_amounts = np.random.randint(1, 6, num_sales)
        sale_ratings = np.random.randint(1, 6, num_sales)
        sales_data = {
            'date': [date for _ in range(num_sales)],
            'customer_id': customer_ids,
            'product_id': product_ids,
            'product_price': product_prices,
            'product_origin': product_origins,
            'sale_amount': sale_amounts,
            'sale_rating': sale_ratings,
        }
        sales = sales.append(pd.DataFrame(sales_data))

# Save the data to a CSV file
sales.to_csv('sales_data.csv', index=False)
