import pandas as pd

# Load data
df = pd.read_csv("data/sales_expense_raw.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Calculate totals
total_revenue = df[df["Type"] == "Revenue"]["Amount"].sum()
total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
net_profit = total_revenue - total_expense

# Expense breakdown
expense_breakdown = (
    df[df["Type"] == "Expense"]
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Percentage contribution
percent_contribution = (expense_breakdown / total_expense) * 100

# Create summary dataframe
summary_df = pd.DataFrame({
    "Metric": ["Total Revenue", "Total Expense", "Net Profit"],
    "Value": [total_revenue, total_expense, net_profit]
})

# Export to Excel
with pd.ExcelWriter("reports/monthly_report.xlsx") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    expense_breakdown.to_excel(writer, sheet_name="Expense Breakdown")
    percent_contribution.to_excel(writer, sheet_name="Expense % Contribution")

print("Report Generated Successfully.")
