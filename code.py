import pandas as pd  # for data manupulation
import plotly.express as px  # for plotting
import streamlit as st  #for webapp

# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="KPIs", page_icon=":seedling:", layout="wide")

# ---- READ DATASET ----
@st.cache

def read_data():
    df = pd.read_csv("productsRatings.csv")
    duplicates = df.duplicated()
    df = df.drop_duplicates()
# Adding the sales
    df["totals"] = df.units_sold*df.retail_price
    return df

df = read_data()

#print(df)


# ---- THE SIDEBAR ----
st.sidebar.header("Adjust Filters:")
origin_country = st.sidebar.multiselect(
    "Select the origin_country:",
    options=df["origin_country"].unique(),
    default=df["origin_country"].unique()
)

merchant_has_profile_picture = st.sidebar.multiselect(
    "Select yes/no image available of merchant:",
    options=df["merchant_has_profile_picture"].unique(),
    default=df["merchant_has_profile_picture"].unique(),
)

uses_ad_boosts = st.sidebar.multiselect(
    "Select yes/no use of ad boost:",
    options=df["uses_ad_boosts"].unique(),
    default=df["uses_ad_boosts"].unique()
)

df_selection = df.query(
    "origin_country == @origin_country & merchant_has_profile_picture ==@merchant_has_profile_picture & uses_ad_boosts == @uses_ad_boosts"
)

# ---- MAINPAGE ----
st.title(":seedling: KPIs")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["totals"].sum())
average_rating = round(df_selection["rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["totals"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")


st.markdown("""---""")
st.title(":chart_with_upwards_trend: Plots")
# SALES BY PRODUCT LINE [BAR CHART]

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
