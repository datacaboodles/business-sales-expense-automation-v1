# Logic Walkthrough – Version 1

Step 1: Load data from CSV
Reason: Convert flat file into structured DataFrame.

Step 2: Calculate Total Revenue
Logic:
- Filter rows where Type == "Revenue"
- Select Amount column
- Apply sum()

Step 3: Calculate Total Expense
Logic:
- Filter rows where Type == "Expense"
- Select Amount column
- Apply sum()

Step 4: Calculate Net Profit
Net Profit = Total Revenue - Total Expense

Step 5: Expense Breakdown
Logic:
- Filter expense rows
- Group by Category
- Sum Amount

Step 6: Percentage Contribution
Logic:
- Divide category expense by total expense
- Multiply by 100

Step 7: Export Report
Use ExcelWriter to create:
- Summary sheet
- Expense Breakdown sheet
