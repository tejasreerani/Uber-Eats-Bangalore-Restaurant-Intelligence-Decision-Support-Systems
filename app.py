import streamlit as st
import pandas as pd
import json
import sqlite3

# Load CSV
df = pd.read_csv("E:/vscode/Uber_Eats_Project/Uber_Eats_data.csv")

# df = Restaurant_Data, df1 = "Orders_Data"

#connecting to database 

conn=sqlite3.connect('Uber_Eats.db')
mycursor=conn.cursor()

st.markdown("""
<style>
/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #F3E5F5;
}

/* Navigation title color */
[data-testid="stSidebar"] .stRadio > label {
    color: Black !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigation", ["Home", "Dashboard"])

if page == "Home":

    st.markdown(
    "<h1 style='color:Purple;'>Uber Eats Bangalore Restaurant Intelligence & Decision Support Systems</h1>",
    unsafe_allow_html=True
)
    st.subheader("**Comprehensive Data_Driven Analysis for Restaurant Performance and Decision Support**")

    st.markdown(
    "<h4 style='color:Purple;'><b>Project Submission By Kurmapu Lakshmi Tejasree</b></h4>",
    unsafe_allow_html=True
)

    st.write("""
    This dashboard analyzes Uber Eats restaurant data to understand:

    • Restaurant ratings  
    • Popular cuisines  
    • Order trends  
    • Payment methods  
    • Discounts usage  
    • Customer behavior  
    """)

    st.image("https://cdn-icons-png.flaticon.com/512/1404/1404945.png", width=200)

    st.sidebar.header("Filters")

    online_order = st.sidebar.selectbox(
    "Select Online Order",
      df["online_order"].dropna().unique()
    )

    rest_type = st.sidebar.selectbox(
    "Select Restaurant Type",
      df["rest_type"].dropna().unique()
    )

    location = st.sidebar.selectbox(
    "Select Location",
     df["location"].dropna().unique()
    )

# Apply main filters first
    filtered_df = df[
     (df["online_order"] == online_order) &
     (df["rest_type"].str.contains(rest_type, na=False)) &
     (df["location"] == location)
    ]

# Cuisine filter from filtered data
    cuisine = st.sidebar.selectbox(
    "Select Cuisine",
     filtered_df["cuisines"].dropna().unique()
    )

    filtered_df = filtered_df[
     filtered_df["cuisines"].str.contains(cuisine, na=False)
    ]

    st.write("Number of Restaurants:", filtered_df.shape[0])
    st.dataframe(filtered_df)

    
elif page == "Dashboard":

     st.title("Uber Eats Restaurant_Data Analysis Dashboard")


     question = st.selectbox(
    "Select Question",
    [
        "Select Question",
        "Which Bangalore locations have the highest average restaurant ratings?",
        "Which locations are over-saturated with restaurants?",
        "Does online ordering improve restaurant ratings?",
        "Does table booking correlate with higher customer ratings?",
        "What price range delivers the best customer satisfaction?",
        "Which cuisines are most common in Bangalore?",
        "Which cuisines receive the highest average ratings?",
        "Which cuisines perform well despite having fewer restaurants?",
        "What is the relationship between restaurant cost and rating?",
        "Do restaurants offering both online ordering and table booking perform better?",
        "Which locations are ideal for premium restaurant onboarding?",
        ]
    )

     if question == "Which Bangalore locations have the highest average restaurant ratings?":

      query = """
      SELECT
      location,
      AVG(rate) AS AVG_Rating
      FROM Restaurant_Data
      GROUP BY location
      ORDER BY AVG_Rating DESC
      LIMIT 15
      """
      df = pd.read_sql_query(query, conn)
      st.subheader("Top Bangalore Locations by Average Rating")
      st.dataframe(df)

     if question == "Which locations are over-saturated with restaurants?":  
   
      query = """SELECT
     location, count(name) as Restaurant_count
     From Restaurant_Data
     Group by location
     Order by Restaurant_count DESC
     LIMIT 15
     """
      df=pd.read_sql_query(query,conn)
      st.subheader("Top Bangalore Locations by Restaurant_Count")
      st.dataframe(df) 
      

     if question == "Does online ordering improve restaurant ratings?":
      query = """SELECT
     online_order, AVG(rate) as Restaurant_Rating
     FROM Restaurant_Data
     Group by Online_order
     Order by Restaurant_Rating DESC
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Online Ordering vs Restaurant Ratings")
      st.dataframe(df)
   

     if question == "Does table booking correlate with higher customer ratings?":
      query = """SELECT
      book_table, AVG(rate) as Restaurant_Rating
     FROM Restaurant_Data
     Group by book_table
     Order by Restaurant_Rating DESC
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Table_booking vs Customer Ratings")
      st.dataframe(df)
  
     if question == "What price range delivers the best customer satisfaction?":
      query = """SELECT
     approx_cost, AVG(rate) as Restaurant_Rating
     FROM Restaurant_Data
     Group by approx_cost
     order by Restaurant_Rating DESC
     LIMIT 15
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Price Vs Customer Satisfaction")
      st.dataframe(df)

     if question == "Which cuisines are most common in Bangalore?":
      query = """SELECT
     cuisines, count(name) as Restaurant_count
     FROM Restaurant_Data
     Group by cuisines
     order by Restaurant_count DESC
     LIMIT 15
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Common cuisines in banglore")
      st.dataframe(df)

     if question == "Which cuisines receive the highest average ratings?":
      query = """SELECT
     cuisines, AVG(rate) as AVG_Restaurant_Rating
     FROM Restaurant_Data
     WHERE cuisines LIKE '%American%'
     Group by cuisines
     order by AVG_Restaurant_Rating DESC
     LIMIT 20
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Cuisines Vs Ratings")
      st.dataframe(df)
   
     if question == "Which cuisines perform well despite having fewer restaurants?":
      query = """SELECT
     cuisines, count(name) as Restaurant_Count, AVG(rate) as AVG_Restaurant_Rating
     FROM Restaurant_Data
     WHERE cuisines LIKE '%Andhra%' and cuisines Like '%Biryani%'
     Group by cuisines
     order by Restaurant_Count
     LIMIT 20
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Best Performing Low-Availability Cuisines")
      st.dataframe(df)

     if question == "What is the relationship between restaurant cost and rating?":
      query = """SELECT
     approx_cost, AVG(rate) as AVG_Restaurant_Rating
     FROM Restaurant_Data
     Group by approx_cost
     order by AVG_Restaurant_Rating DESC
     LIMIT 15
     """
      df=pd.read_sql_query(query,conn)
      st.subheader("Impact of Restaurant Cost on Ratings")
      st.dataframe(df)

     if question == "Do restaurants offering both online ordering and table booking perform better?":
      query = """SELECT
     online_order, book_table, AVG(rate) as AVG_Restaurant_Rating
     FROM Restaurant_Data
     Group by online_order, book_table
     order by AVG_Restaurant_Rating DESC
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Restaurant Performance Based on Service Availability")
      st.dataframe(df)

     if question == "Which locations are ideal for premium restaurant onboarding?":
      query = """SELECT
     location, Avg(rate) as AVG_Restaurant_Rating
     FROM Restaurant_Data
     Group by location
     order by AVG_Restaurant_Rating DESC
     LIMIT 15
     """
      df = pd.read_sql_query(query,conn)
      st.subheader("Top Locations Suitable for Premium Restaurant Onboarding")
      st.dataframe(df)

# Load JSON
     df1=pd.read_json("E:/vscode/Uber_Eats_Project/orders.json")

     conn=sqlite3.connect('Uber_Eats.db')
     mycursor=conn.cursor()

# Create table
     mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_name VARCHAR(100) NOT NULL,
    order_date VARCHAR(50),
    order_value DECIMAL(10,2),
    discount_used VARCHAR(50),
    payment_method VARCHAR(50)
    )
    """)

# Save changes
     conn.commit()

     # st.success("Orders table created successfully!")

# Insert data into table

     query = """
     INSERT INTO Orders
     (restaurant_name, order_date, order_value,
     discount_used, payment_method)
     VALUES (?, ?, ?, ?, ?)
     """

     data = df1[['restaurant_name',
            'order_date',
            'order_value',
            'discount_used',
            'payment_method']].values.tolist()

     mycursor.executemany(query, data)
     conn.commit()

     # st.success("Data inserted successfully!")

     st.title("Order_Data Analysis Dashboard")

     question = st.selectbox(
     "Select Question",
     [
        "Select Question",
        "What is the total order_value on order_date 2026-01-22?",
        "What is the relationship between order_value and discount_used?",
        "Most used payment method?",
        "will discount increase order value?",
        "Which restaurant generates highest revenue?",
        "Which date had highest revenue?",
        "On which order_date discounts are used the most?",
        "what is the order date where highest no:of orders taken place in restaurant?",
        ]
    )

     if question == "What is the total order_value on order_date 2026-01-22?":
      query = """SELECT
     order_date, sum(order_value) as Total_Order_Value
     FROM Orders
     WHERE order_date = '2026-01-22'
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Total Order Value on 22 Jan 2026")
      st.dataframe(df1)

     if question == "What is the relationship between order_value and discount_used?":
      query = """SELECT
     discount_used, AVG(order_value) as AVG_Order_Value
     FROM Orders
     Group by discount_used
     order by AVG_order_value DESC
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Relationship between order_value and Discount_used")
      st.dataframe(df1)

     if question == "Most used payment method?":
      query = """SELECT
     payment_method, count(payment_method) as Payment_Method_Count
     FROM Orders
     Group by payment_method
     order by Payment_Method_Count
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Highly used payment method")
      st.dataframe(df1)

     if question == "will discount increase order value?":
      query = """SELECT
     discount_used, AVG(order_value) as AVG_Order_Value
     FROM Orders
     Group by discount_used
     order by AVG_order_value DESC
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Impact of Discounts on Order Value")
      st.dataframe(df1)

     if question == "Which restaurant generates highest revenue?":
      query = """SELECT
     restaurant_name, sum(order_value) as Total_Revenue
     FROM Orders
     Group by restaurant_name
     order by Total_Revenue DESC
     LIMIT 16
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Top Revenue Generating Restaurant")
      st.dataframe(df1)

     if question == "Which date had highest revenue?":
      query = """SELECT
     order_date, sum(order_value) as Revenue
     From orders
     Group by order_date
     order by Revenue DESC
     LIMIT 10
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Top Revenue Generating Date")
      st.dataframe(df1)

     if question == "On which order_date discounts are used the most?":
      query = """SELECT
     order_date, count(discount_used) as Total_Discounts
     FROM orders
     GROUP BY order_date
     ORDER BY Total_Discounts DESC
     LIMIT 15
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Discount Usage Trend by Date")
      st.dataframe(df1)

     if question == "what is the order date where highest no:of orders taken place in restaurant?":
      query = """SELECT
     order_date, restaurant_name, count(restaurant_name) as Highest_orders
     FROM orders
     group by order_date, restaurant_name
     order by Highest_orders DESC
     limit 20
     """
      df1 = pd.read_sql_query(query,conn)
      st.subheader("Maximum Orders Recorded on a Date")
      st.dataframe(df1)
   
   





