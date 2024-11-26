# Sort and aggregate the data in a table using HiveQL #

### **Aim:**
To write queries to sort and aggregate the data in a table using HiveQL
---

### **Procedure:**
Step 1: **Set up Hive**: Start Hive shell using `hive`.

Step 2: **Create Table**: Define table using `CREATE TABLE`.

Step 3: **Load Data**: Load data using `LOAD DATA`.

Step 4: **Sort Data**: Use `ORDER BY` to sort data.

Step 5: **Aggregate Data**: Use `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` with `GROUP BY`.

---

### **Program:**

```sql
-- Create table
CREATE TABLE sales_data (
    id INT,
    product_name STRING,
    category STRING,
    sales_amount FLOAT,
    region STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',' STORED AS TEXTFILE;
```
```sql
-- Load data
LOAD DATA LOCAL INPATH '/path/to/sales_data.csv' INTO TABLE sales_data;
```
```sql
-- Sort data by sales_amount descending
SELECT * FROM sales_data ORDER BY sales_amount DESC;
```
```sql
-- Aggregation Queries

-- Count rows in each category
SELECT category, COUNT(*) AS sales_count FROM sales_data GROUP BY category;

-- Total sales in each category
SELECT category, SUM(sales_amount) AS total_sales FROM sales_data GROUP BY category;

-- Average sales in each category
SELECT category, AVG(sales_amount) AS avg_sales FROM sales_data GROUP BY category;

-- Maximum sales in each category
SELECT category, MAX(sales_amount) AS max_sales FROM sales_data GROUP BY category;

-- Minimum sales in each category
SELECT category, MIN(sales_amount) AS min_sales FROM sales_data GROUP BY category;
```

---

### **Input:**

```csv
1,Smartphone,Electronics,1000,North
2,Laptop,Electronics,2000,South
3,Shirt,Clothing,500,North
4,Jeans,Clothing,700,East
5,Watch,Accessories,300,West
6,Tablet,Electronics,1500,North
7,Bag,Accessories,200,South
```

---

### **Output:**

1. **Sorted Data** (by `sales_amount` descending):
```sql
| ID  | Product Name | Category     | Sales Amount | Region  |
|-----|--------------|--------------|--------------|---------|
| 2   | Laptop       | Electronics  | 2000         | South   |
| 6   | Tablet       | Electronics  | 1500         | North   |
| 1   | Smartphone   | Electronics  | 1000         | North   |
| 4   | Jeans        | Clothing     | 700          | East    |
| 3   | Shirt        | Clothing     | 500          | North   |
| 5   | Watch        | Accessories  | 300          | West    |
| 7   | Bag          | Accessories  | 200          | South   |
```

2. **COUNT** (Number of rows per category):
```sql
| Category     | Sales Count |
|--------------|-------------|
| Electronics  | 3           |
| Clothing     | 2           |
| Accessories  | 2           |
```

3. **SUM** (Total sales per category):
```sql
| Category     | Total Sales |
|--------------|-------------|
| Electronics  | 4500        |
| Clothing     | 1200        |
| Accessories  | 500         |
```

4. **AVG** (Average sales per category):
```sql
| Category     | Avg Sales   |
|--------------|-------------|
| Electronics  | 1500        |
| Clothing     | 600         |
| Accessories  | 250         |
```

5. **MAX** (Maximum sales per category):
```sql
| Category     | Max Sales   |
|--------------|-------------|
| Electronics  | 2000        |
| Clothing     | 700         |
| Accessories  | 300         |
```

6. **MIN** (Minimum sales per category):
```sql
| Category     | Min Sales   |
|--------------|-------------|
| Electronics  | 1000        |
| Clothing     | 500         |
| Accessories  | 200         |
```

---

### **Result:**
The queries successfully sorted the data by `sales_amount` and aggregated the data using `COUNT`, `SUM`, `AVG`, `MAX`, and `MIN` functions to analyze the dataset.

---
