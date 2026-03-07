import pandas as pd
import numpy as np
import sqlite3
import streamlit

# Read CSV file
df=pd.read_csv('Uber_Eats_data.csv')
df

# Connect to sqlite3 database
conn=sqlite3.connect('Uber_Eats.db')
mycursor=conn.cursor()

# Remove duplicates & data cleaning

df=df.drop_duplicates()

# Cleaning the data

def clean_rate(x):
    if isinstance(x, str) and "/" in x:
        return float(x.split("/")[0])
    else:
        return None

df.loc[:, "rate"] = df["rate"].apply(clean_rate)

df.columns = ['name', 'online_order', 'book_table', 'rate', 'votes', 'phone', 'location', 'rest_type', 'dish_liked', 'cuisines', 'approx_cost', 'listed_type', 'listed_city']
df.columns

data=df.values.tolist()
data

# Create a table

mycursor.execute("""CREATE TABLE if not EXISTS Restaurant_Data (

                 name VARCHAR(100) NOT NULL,
                 online_order VARCHAR(50),
                 book_table VARCHAR(50),
                 rate DECIMAL(3,1),
                 votes INT,
                 phone VARCHAR (50),
                 location VARCHAR(100),
                 rest_type VARCHAR(100),
                 dish_liked TEXT,
                 cuisines VARCHAR(300),
                 approx_cost DECIMAL(10,2),
                 listed_type VARCHAR(100),
                 listed_city VARCHAR (100)

                 )""")
conn.commit()

# Insert data into table

query = """INSERT INTO Restaurant_Data
(name, online_order, book_table, rate, votes,
phone, location, rest_type, dish_liked, cuisines,
approx_cost, listed_type, listed_city)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

mycursor.executemany(query,data)
conn.commit()

# Select entire data

import pandas as pd

query = "SELECT * FROM Restaurant_Data"
df = pd.read_sql_query(query, conn)
df

# Applying filters for the given data

query = """SELECT *
FROM Restaurant_Data
WHERE
online_order = 'Yes' AND
rest_type = 'Delivery' AND
approx_cost < 500 AND
votes < 400 AND
listed_type = 'Delivery'
"""
df = pd.read_sql_query(query, conn)
df

# 1. Which Bangalore locations have the highest average restaurant ratings?

query = """SELECT
location, AVG(rate) as AVG_Rating
FROM Restaurant_Data
GROUP BY location
ORDER BY AVG_Rating DESC
LIMIT 15
"""
df = pd.read_sql_query(query, conn)
df

# 2. Which locations are over-saturated with restaurants?

query = """SELECT
location, count(name) as Restaurant_count
From Restaurant_Data
Group by location
Order by Restaurant_count DESC
LIMIT 15
"""
df=pd.read_sql_query(query,conn)
df

# 3. Does online ordering improve restaurant ratings?

query = """SELECT
online_order, AVG(rate) as Restaurant_Rating
FROM Restaurant_Data
Group by Online_order
Order by Restaurant_Rating DESC
"""
df = pd.read_sql_query(query,conn)
df

# 4. Does table booking correlate with higher customer ratings?

query = """SELECT
book_table, AVG(rate) as Restaurant_Rating
FROM Restaurant_Data
Group by book_table
Order by Restaurant_Rating DESC
"""
df = pd.read_sql_query(query,conn)
df

# 5. What price range delivers the best customer satisfaction?

query = """SELECT
approx_cost, AVG(rate) as Restaurant_Rating
FROM Restaurant_Data
Group by approx_cost
order by Restaurant_Rating DESC
LIMIT 15
"""
df = pd.read_sql_query(query,conn)
df

# 6. Which cuisines are most common in Bangalore?

query = """SELECT
cuisines, count(name) as Restaurant_count
FROM Restaurant_Data
Group by cuisines
order by Restaurant_count DESC
LIMIT 15
"""
df = pd.read_sql_query(query,conn)
df

# 7. Which cuisines receive the highest average ratings?  check

query = """SELECT
cuisines, AVG(rate) as AVG_Restaurant_Rating
FROM Restaurant_Data
WHERE cuisines LIKE '%American%'
Group by cuisines
order by AVG_Restaurant_Rating DESC
LIMIT 20
"""
df = pd.read_sql_query(query,conn)
df

# 8. Which cuisines perform well despite having fewer restaurants?

query = """SELECT
cuisines, count(name) as Restaurant_Count, AVG(rate) as AVG_Restaurant_Rating
FROM Restaurant_Data
WHERE cuisines LIKE '%Andhra%' and cuisines Like '%Biryani%'
Group by cuisines
order by Restaurant_Count
LIMIT 20
"""

df = pd.read_sql_query(query,conn)
df

# 9. What is the relationship between restaurant cost and rating?

query = """SELECT
approx_cost, AVG(rate) as AVG_Restaurant_Rating
FROM Restaurant_Data
Group by approx_cost
order by AVG_Restaurant_Rating DESC
LIMIT 15
"""
df=pd.read_sql_query(query,conn)
df

# 10. Do restaurants offering both online ordering and table booking perform better?

query = """SELECT
online_order, book_table, AVG(rate) as AVG_Restaurant_Rating
FROM Restaurant_Data
Group by online_order, book_table
order by AVG_Restaurant_Rating DESC
"""
df = pd.read_sql_query(query,conn)
df

# 11. Which locations are ideal for premium restaurant onboarding?

query = """SELECT
location, Avg(rate) as AVG_Restaurant_Rating
FROM Restaurant_Data
Group by location
order by AVG_Restaurant_Rating DESC
LIMIT 15
"""
df = pd.read_sql_query(query,conn)
df

# Adding and Reading json file

df1=pd.read_json("orders.json")
df1

df1.columns

data=df1.values.tolist()
data

# create a table

mycursor.execute("""
CREATE TABLE if not EXISTS Orders (
                 order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 restaurant_name VARCHAR(100) NOT NULL,
                 order_date VARCHAR(50),
                 order_value DECIMAL(3,1),
                 discount_used VARCHAR (50),
                 payment_method VARCHAR (50)
                 )""")
conn.commit()

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

df1.drop_duplicates()

# 1. What is the total order_value on order_date 2026-01-22?

query = """SELECT
order_date, sum(order_value) as Total_Order_Value
FROM Orders
WHERE order_date = '2026-01-22'
"""
df1 = pd.read_sql_query(query,conn)
df1

# 2. What is the relationship between order_value and discount_used?

query = """SELECT
discount_used, AVG(order_value) as AVG_Order_Value
FROM Orders
Group by discount_used
order by AVG_order_value DESC
"""

df1 = pd.read_sql_query(query,conn)
df1

# 3. Most used payment method?

query = """SELECT
payment_method, count(payment_method) as Payment_Method_Count
FROM Orders
Group by payment_method
order by Payment_Method_Count
"""

df1 = pd.read_sql_query(query,conn)
df1

# 4. will discount increase order value?

query = """SELECT
discount_used, AVG(order_value) as AVG_Order_Value
FROM Orders
Group by discount_used
order by AVG_order_value DESC
"""

df1 = pd.read_sql_query(query,conn)
df1

# 5. Which restaurant generates highest revenue?

query = """SELECT
restaurant_name, sum(order_value) as Total_Revenue
FROM Orders
Group by restaurant_name
order by Total_Revenue DESC
LIMIT 16
"""

df1 = pd.read_sql_query(query,conn)
df1

# 6. Which date had highest revenue?

query = """SELECT
order_date, sum(order_value) as Revenue
From orders
Group by order_date
order by Revenue DESC
LIMIT 10
"""

df1 = pd.read_sql_query(query,conn)
df1

# 7. on which order_date discounts are used the most?

query = """SELECT
order_date, count(discount_used) as Total_Discounts
FROM orders
GROUP BY order_date
ORDER BY Total_Discounts DESC
LIMIT 15
"""

df1 = pd.read_sql_query(query,conn)
df1

# 8. what is the order date where highest no:of orders taken place in restaurant?

query = """SELECT
order_date, restaurant_name, count(restaurant_name) as Highest_orders
FROM orders
group by order_date, restaurant_name
order by Highest_orders DESC
limit 20
"""

df1 = pd.read_sql_query(query,conn)
df1

