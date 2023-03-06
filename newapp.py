import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Read in data
data = pd.read_csv("sales_data.csv")

# Sidebar filters
st.sidebar.title("Filters")
location_filter = st.sidebar.selectbox("Select location", ["All"] + data["Origin Country"].unique().tolist())
price_range_filter = st.sidebar.slider("Select price range", 100, 4000, (100, 4000), step=100)
rating_filter = st.sidebar.slider("Select minimum rating", 1, 5, 1)

# Filter data based on sidebar filters
filtered_data = data[(data["Origin Country"] == location_filter) | (location_filter == "All")]
filtered_data = filtered_data[(filtered_data["Sales Price"] >= price_range_filter[0]) & (filtered_data["Sales Price"] <= price_range_filter[1])]
filtered_data = filtered_data[filtered_data["Rating"] >= rating_filter]

# Calculate KPIs
total_sales = filtered_data["Sales"].sum()
avg_sales = filtered_data["Sales"].mean()
avg_rating = filtered_data["Rating"].mean()
avg_sales_per_transaction = filtered_data.groupby("Transaction ID")["Sales"].sum().mean()

# Monthly sales plot
monthly_sales = filtered_data.groupby(pd.Grouper(key="Order Date", freq="M")).sum().reset_index()
monthly_sales_fig = px.line(monthly_sales, x="Order Date", y="Sales", title="Monthly Sales")
st.plotly_chart(monthly_sales_fig)

# Yearly profit and ratings barcharts
yearly_data = filtered_data.groupby(pd.Grouper(key="Order Date", freq="Y")).sum().reset_index()
yearly_fig = px.bar(yearly_data, x="Order Date", y="Profit", title="Yearly Profit and Ratings")
yearly_fig.add_trace(px.bar(yearly_data, x="Order Date", y="Rating", title="Yearly Profit and Ratings").data[0])
yearly_fig.update_layout(barmode="group")
st.plotly_chart(yearly_fig)

# Display KPIs
st.write(f"Total Sales: ${total_sales:.2f}")
st.write(f"Average Sales: ${avg_sales:.2f}")
st.write(f"Average Rating: {avg_rating:.2f}")
st.write(f"Average Sales per Transaction: ${avg_sales_per_transaction:.2f}")
