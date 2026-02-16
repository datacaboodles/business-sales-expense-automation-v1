# Theory Notes – Version 1

## Key Pandas Concepts Used

### 1. Filtering
df[df["Type"] == "Expense"]

Creates a Boolean mask and filters rows.

### 2. Column Selection
["Amount"]

Selects a specific column for aggregation.

### 3. Aggregation
.sum()

Calculates total value.

### 4. Grouping
.groupby("Category")

Splits data into virtual groups for aggregation.

### 5. Sorting
.sort_values(ascending=False)

Ranks values highest to lowest.

---

## Business Logic

Revenue = Money In  
Expense = Money Out  
Net Profit = Revenue - Expense  

Sorting expenses helps identify major cost drivers.

Percentage contribution helps prioritize cost control.
