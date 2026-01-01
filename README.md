# Store Sales Analysis — SQLite + Python Project

## Overview
This project analyzes sales data for a small retail store using SQLite and Python.  
It demonstrates skills in:

- SQL data cleaning  
- Database design  
- Python data analysis  
- Data visualization  
- Exporting results  

---

## Dataset
The project uses two tables:

- `PRODUCTS_CLEAN` — product information  
- `SALES_CLEAN` — sales transactions  

Both tables were cleaned and validated using SQL.

---

## SQL Join
The final dataset is created using:

```sql
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
    ON S.PRODUCT_ID = P.PRODUCT_ID;
```

---

## Visualizations
The analysis includes:

- Revenue by product  
- Revenue by category  
- Daily revenue trend  

Charts were created using matplotlib.

---

## Exported Results
- `final_sales_analysis.csv`

---

## Technologies Used
- SQLite  
- Python  
- Pandas  
- Matplotlib  

---

## Business Insights
- Top‑selling products  
- Most profitable categories  
- Sales trends across January  
- Recommendations for inventory  

---

## Purpose
This project demonstrates practical data analysis skills suitable for:

- Junior Data Analyst roles  
- Business Intelligence roles  
- SQL/Python analyst positions  

