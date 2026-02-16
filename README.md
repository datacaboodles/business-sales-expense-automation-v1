# Business Sales & Expense Automation – Version 1

## Overview
This project automates monthly financial reporting using Python (Pandas).

It calculates:
- Total Revenue
- Total Expense
- Net Profit
- Expense Breakdown by Category
- Percentage Contribution of Each Expense Category

This is Version 1 using a clean dataset.

Future versions will handle:
- Messy / inconsistent weekly client data
- Data validation
- Schema standardization
- Automation-ready scripts

---

## Business Problem

Small businesses often:
- Track revenue and expenses in Excel
- Manually calculate totals
- Lack clarity on expense distribution

This script converts raw CSV data into structured financial insights automatically.

---

## Dataset Structure

Columns:
- Date
- Category
- Amount
- Type (Revenue / Expense)

---

## Key KPIs Computed

1. Total Revenue
2. Total Expense
3. Net Profit (Revenue - Expense)
4. Expense Breakdown by Category
5. Expense Percentage Contribution

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run script:

python scripts/generate_report.py

Output:
- monthly_report.xlsx generated in reports/

---

## Technologies Used

- Python
- Pandas
- Excel Export

---

## Versioning

Version 1:
- Clean dataset
- Manual CSV upload
- Basic automation

Version 2 (Planned):
- Messy data handling
- Schema validation
- Duplicate detection
- Missing value handling
- Logging system
