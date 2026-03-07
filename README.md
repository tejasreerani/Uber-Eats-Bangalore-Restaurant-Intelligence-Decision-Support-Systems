# 🍽️ Uber_Eats Banglore Restaurant Data Analysis Dashboard

## 📌 Project Overview

This project analyzes restaurant data from the Uber_Eats dataset using **Python, SQLite, Pandas, and Streamlit**.
The goal of the project is to extract meaningful insights about restaurants such as ratings, cuisines, locations, and cost using **SQL queries and interactive dashboard visualizations**.

The dashboard allows users to filter restaurant data and explore different business insights interactively.

---

## 🎯 Objectives

* Analyze restaurant performance across different locations.
* Understand the relationship between cost and ratings.
* Identify popular cuisines and restaurant types.
* Analyze the impact of online ordering and table booking on ratings.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **SQLite3**
* **Streamlit**
* **SQL**

---

## 📂 Restaurant_Dataset Description

The dataset contains information about restaurants listed on Uber_Eats including:

* Restaurant Name
* Online Order Availability
* Table Booking Availability
* Rating
* Number of Votes
* Phone Number
* Location
* Restaurant Type
* Popular Dishes
* Cuisines Offered
* Approximate Cost for Two People
* Listed Type
* Listed City

## 📂 Orders_Dataset Description:

The dataset contains information about restaurants listed on Uber_Eats including:

* Order_id
* Restaurant_name
* Order_date
* Order_value
* Discount_used
* Payment_method
---

## 📊 Key Business Questions Answered (Restaurant_Dataset)

1. Which Bangalore locations have the highest average restaurant ratings?
2. Does online ordering improve restaurant ratings?
3. Which cuisines perform well despite having fewer restaurants?
4. What is the relationship between restaurant cost and rating?
5. Do restaurants offering both online ordering and table booking perform better?
6. Which locations are ideal for premium restaurant onboarding?
7. Which locations are over_saturated with restaurants?
8. Does table_booking correlate with higher customer ratings?
9. What price range delivers the best customer satisfaction?
10. Which cuisines are most common in banglore?
11. Which cuisine receives highest average ratings?

## 📊 Key Business Questions Answered (Orders_Dataset)

1. What is the total order_value on order_date 2026-01-22?
2. What is the relationship between order_value and discount_used?
3. Most used payment method?
4. will discount increase order value?
5. Which restaurant generates highest revenue?
6. Which date had highest revenue?
7. On which order_date discounts are used the most?
8. what is the order date where highest no:of orders taken place in restaurant?

---

## 📁 Project Structure

```
Uber_Eats-Dashboard
│
├── app.py                                            # Streamlit dashboard application
├── 01_Uber_Eats_Restaurant_Intelligence.py           # SQLite database creation and data insertion
├── Uber_Eats_data.csv                                # Dataset file
├── orders.json                                       # Dataset file
└── README.md                                         # Project documentation


```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```
https://github.com/tejasreerani/Uber-Eats-Bangalore-Restaurant-Intelligence-Decision-Support-Systems.git
```

### Step 2: Install Required Libraries

```
pip install pandas streamlit sqlite3
```

### Step 3: Run the Streamlit App

```
streamlit run app.py
```

---

## 📷 Dashboard Preview

### Home Page

<img width="744" height="475" alt="image" src="https://github.com/user-attachments/assets/c8670ff2-a9ae-4900-8686-928d1af96a5b" />

### Filters Section

<img width="787" height="397" alt="image" src="https://github.com/user-attachments/assets/b5021c05-3e8f-4a46-97c6-b49588452791" />

### Data Insights

<img width="769" height="479" alt="image" src="https://github.com/user-attachments/assets/2f844d7d-1a23-4609-9aa8-4b7148b1498e" />


---

## 📈 Features of the Dashboard

✔ Interactive filters for restaurant data
✔ SQL based data analysis
✔ Location-wise restaurant insights
✔ Cuisine performance analysis
✔ Cost vs Rating analysis
✔ Online ordering and booking insights

---

## 👩‍💻 Author

**Tejasree Rani**

---

## 📌 Conclusion

This project demonstrates how **SQL, Python, and Streamlit** can be used together to build an interactive data analytics dashboard.
The insights generated can help restaurant businesses understand customer preferences and improve decision making.
