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
https://github.com/abdolreza-tech/store-sales-analysis/blob/f7b938182d98b0608e991b5bc3fbc8e41ad659e3/Figure_1.png
https://github.com/abdolreza-tech/store-sales-analysis/blob/7277a417de44d1cdb29bba874e2a0a5e756ab808/Figure_2.png
https://github.com/abdolreza-tech/store-sales-analysis/blob/666977cb5eb1acbf16aae18191f7c020aefe5b65/Figure_3.png
https://github.com/abdolreza-tech/store-sales-analysis/blob/a5cffec5aa5bfd03ea6006bc948bf48bc70c2dcf/Figure_4.png
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
## Business Insights

### 1. Top-Selling Products
- PEN generated the highest total revenue due to multiple sales entries.
- NOTEBOOK and COFFE also performed strongly.

### 2. Most Profitable Categories
- FOOD products generated the highest total revenue.
- STATIONARY products had more transactions but lower average price.

### 3. Sales Trends
- Sales peaked around mid-January.
- The highest revenue day was 2024-01-12.

### 4. Recommendations
- Increase stock of PEN, NOTEBOOK, and COFFE.
- Consider promotions for lower-performing stationary items.
- Analyze customer behavior on peak days to optimize staffing. 

---

## Purpose
This project demonstrates practical data analysis skills suitable for:

- Junior Data Analyst roles  
- Business Intelligence roles  
- SQL/Python analyst positions  







