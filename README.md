# 📦 PeakFit Inventory Analysis

This project analyzes inventory discrepancies from the PeakFit Essentials store using Python and interactive dashboards. The goal is to identify abnormal shortages or surpluses in inventory and recommend improvements.

## 📁 Dataset
- **Source:** `PeakFit Essentials.xlsx`
- **Period:** 01/01/2024 – 30/09/2024
- **Fields Used:** Date, Shift, Staff, Item, Category, Actual Quantity, Expected Quantity

## 🎯 Objectives
- Detect dates, shifts, and staff with the most discrepancies
- Highlight problematic items with high shortage
- Visualize trends with interactive charts
- Provide actionable recommendations

## 🧹 Data Cleaning
- Removed unnecessary columns (returns, expired, etc.)
- Extracted date features: month, weekday
- Computed inventory discrepancy = `Actual - Expected`
- Mapped items to categories manually

## 📊 Visualizations
- **Heatmap Calendar** – Daily discrepancy values
- **Bar Charts** – Top problem staff, weekdays
- **Line Chart** – Discrepancies by shift
- **Item-Level Analysis** – Top 2 worst-performing items
- **Interactive Dashboard** – Filters by date, staff, item, etc.
- **KPI Panel** – Total shortage, surplus, and peak days

## 🛠️ Tools & Libraries
- Python (Jupyter Notebook)
- Pandas & NumPy (data handling)
- Plotly (interactive charts)
- Panel (dashboard)
- datetime (date operations)

## 📁 Files
- `PeakFit_analysis2.ipynb`: Main dashboard notebook
- `PeakFit Essentials.xlsx`: Source dataset
- `requirements.txt`: Python dependencies

## 🚀 How to Run
1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the notebook:
   ```bash
   jupyter notebook PeakFit_analysis2.ipynb
   ```

3. Launch the dashboard from within the notebook using:
   ```python
   dashboard.servable()
   ```

## 📌 Author
Ahmed – Data Analyst & Inventory Specialist
