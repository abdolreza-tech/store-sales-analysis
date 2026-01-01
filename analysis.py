import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to your SQLite database
conn = sqlite3.connect(r"C:\Users\glide\OneDrive\Documents\STORE_PROJECT_PYTHON\STORE_PROJECT.DB")

# SQL query using the CLEAN tables
query = """
SELECT 
    S.SALES_ID,
    S.PRODUCT_ID,
    P.PRODUCT_NAME,
    P.CATEGORY,
    S.QUANTITY,
    P.PRICE,
    S.QUANTITY * P.PRICE AS REVENUE,
    S.SALES_DATE
FROM SALES_CLEAN S
JOIN PRODUCTS_CLEAN P
    ON S.PRODUCT_ID = P.PRODUCT_ID
ORDER BY S.SALES_ID;
"""

df = pd.read_sql_query(query, conn)

print(df.head())

# Plot revenue by product
df.groupby("PRODUCT_NAME")["REVENUE"].sum().plot(kind="bar", color="skyblue")
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby("PRODUCT_NAME")["REVENUE"].sum().plot(kind="bar", color="skyblue")
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby("CATEGORY")["REVENUE"].sum().plot(kind="bar", color="orange")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (€)")
plt.tight_layout()
plt.show()

df.groupby("SALES_DATE")["REVENUE"].sum().plot(kind="line", marker="o")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.to_csv("final_sales_analysis.csv", index=False)