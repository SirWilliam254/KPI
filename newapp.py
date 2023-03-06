import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate some example data
np.random.seed(123)
dates = pd.date_range('20220101', periods=1000)
sales = np.random.normal(loc=100, scale=20, size=1000)
revenue = sales * np.random.uniform(low=0.8, high=1.2, size=1000)
costs = revenue * np.random.uniform(low=0.5, high=0.8, size=1000)
profit = revenue - costs

# Combine the data into a DataFrame
data = pd.DataFrame({'Date': dates, 'Sales': sales, 'Revenue': revenue, 'Costs': costs, 'Profit': profit})

# Create the Streamlit app
st.title('Sales KPI Analysis')
st.write('This app analyzes key performance indicators for a sales business.')

# Show the raw data
st.subheader('Raw Data')
st.write(data)

# Show a line chart of sales over time
st.subheader('Sales Over Time')
fig, ax = plt.subplots()
sns.lineplot(x='Date', y='Sales', data=data, ax=ax)
ax.set(xlabel='Date', ylabel='Sales')
st.pyplot(fig)

# Show a bar chart of revenue and costs over time
st.subheader('Revenue and Costs Over Time')
fig, ax = plt.subplots()
data_melt = pd.melt(data, id_vars='Date', value_vars=['Revenue', 'Costs'], var_name='Metric', value_name='Amount')
sns.barplot(x='Date', y='Amount', hue='Metric', data=data_melt, ax=ax)
ax.set(xlabel='Date', ylabel='Amount')
st.pyplot(fig)

# Show a scatterplot of profit vs. sales
st.subheader('Profit vs. Sales')
fig, ax = plt.subplots()
sns.scatterplot(x='Sales', y='Profit', data=data, ax=ax)
ax.set(xlabel='Sales', ylabel='Profit')
st.pyplot(fig)

# Calculate and show summary statistics
st.subheader('Summary Statistics')
st.write(data[['Sales', 'Revenue', 'Costs', 'Profit']].describe())
