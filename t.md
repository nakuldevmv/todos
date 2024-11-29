### **Aim**  
To demonstrate the usage of NumPy, Pandas, and Matplotlib for data manipulation and visualization.  

---

### **Algorithm**  
1. Import the required libraries: NumPy, Pandas, and Matplotlib.  
2. Create a NumPy array and perform basic operations.  
3. Create a Pandas DataFrame from the NumPy array and manipulate the data.  
4. Visualize the data using Matplotlib.  
5. Display the results.  

---

### **Program**  

```python
# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Step 2: Perform operations on NumPy array
squared_data = data ** 2

# Step 3: Create a Pandas DataFrame
df = pd.DataFrame({'Original': data, 'Squared': squared_data})

# Step 4: Visualize the data using Matplotlib
plt.plot(df['Original'], df['Squared'], marker='o')
plt.title('Original vs Squared Data')
plt.xlabel('Original Data')
plt.ylabel('Squared Data')
plt.grid(True)
plt.show()

# Displaying the DataFrame
print("DataFrame:")
print(df)
```  

---

### **Input**  
The program uses an array of numbers: `[10, 20, 30, 40, 50]`.  

---

### **Output**  
1. A plot displaying the relationship between the original and squared data.  
2. The DataFrame displayed in the terminal:  

```
DataFrame:
   Original  Squared
0        10      100
1        20      400
2        30      900
3        40     1600
4        50     2500
```  

---

### **Result**  
The working of NumPy, Pandas, and Matplotlib was successfully implemented. A DataFrame was created, and the data was visualized in a plot.  

