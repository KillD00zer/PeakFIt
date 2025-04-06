# PeakFit Inventory Analysis Documentation

## 1. Project Overview

This document provides professional documentation for the PeakFit Inventory Analysis project. The project aims to analyze inventory data from PeakFit Essentials, a fitness equipment and supplement store, to identify discrepancies, understand stock patterns, and provide actionable insights for inventory management. The analysis is performed using a Jupyter Notebook (`PeakFIt_analysis2.ipynb`) and generates an interactive dashboard for visualizing key inventory metrics.

## 2. Data Description

The data is sourced from an Excel file named `PeakFit Essentials.xlsx`, sheet 'Sheet1'. It contains inventory records from January 1, 2024, to September 30, 2024. The dataset includes the following key columns:

- **Date**: Date of the inventory record.
- **Time**: Shift time (Morning, Afternoon, Evening).
- **Item ID**: Unique identifier for each item (e.g., ITM001).
- **Category**: Category of the item (e.g., Strength Training Equipment).
- **Expected Quantity**: Expected stock quantity.
- **Actual Quantity**: Actual stock quantity after inventory count.
- **Inventory Discrepancy**: Calculated as `Actual Quantity - Expected Quantity`. This is the primary metric analyzed in this project.
- **Responsible Staff**: Staff member responsible for the inventory record.

The dataset covers 6 items across 3 categories, managed by 6 staff members over three shifts daily.

## 3. Data Cleaning and Processing

The data cleaning and processing steps performed in the Jupyter Notebook are as follows:

1. **Data Loading**: The data is read from the Excel file `PeakFit Essentials.xlsx` using pandas.
2. **Dropping Unnecessary Columns**: Columns like 'Expired Items', 'Returned Items', 'Items Out for Sales', 'Items Out for Quality Control', and 'Items Out for Events' are dropped as they are not relevant to the core inventory discrepancy analysis.
3. **Date Conversion**: The 'Date' column is converted to datetime format for time-series analysis.
4. **Calculating Inventory Discrepancy**: A new column 'Inventory Discrepancy' is calculated by subtracting 'Expected Quantity' from 'Actual Quantity'. The original 'Expected Quantity' and 'Actual Quantity' columns are then dropped.
5. **Month Extraction**: A 'Month' column is extracted from the 'Date' column to facilitate monthly analysis.
6. **Category Correction**: The 'Category' column is corrected to ensure consistency and accuracy. Items are re-categorized as follows:
    - ITM001, ITM003, ITM006 are assigned to 'CTG001' (Strength Training Equipment).
    - ITM004 is assigned to 'CTG003' (Supplements - Protein Powder).
    - ITM005 is assigned to 'CTG004' (Recovery Tools - Foam Rollers).

## 4. Analysis and Visualizations

The Jupyter Notebook generates several visualizations and KPIs to analyze the inventory data:

### 4.1. Calendar Heatmap (Heat_fig)

- **Purpose**: To visualize inventory discrepancies across days and months.
- **Description**: A heatmap is generated where days of the month are on the y-axis and months are on the x-axis. The color intensity represents the magnitude of inventory discrepancy for each day. Red indicates negative discrepancy (missing items), and blue indicates positive discrepancy (overstock).
- **Key Findings**:
    - July 25th shows a significant overstock of 31 items.
    - May 30th and August 3rd show the highest missing records, with approximately 23 items missing on each day.

### 4.2. Weekday Bar Chart (Bar_fig)

- **Purpose**: To analyze inventory discrepancies by weekday.
- **Description**: A bar chart showing the total inventory discrepancy for each day of the week.
- **Key Findings**:
    - Tuesdays consistently show the highest negative inventory discrepancy, with about 94 items missing in total over the analyzed period. This suggests potential issues with inventory management on Tuesdays.

### 4.3. Staff Performance Analysis (Bar2_fig)

- **Purpose**: To identify staff members with the most significant inventory discrepancies.
- **Description**: A bar chart showing the sum of inventory discrepancies attributed to each responsible staff member.
- **Key Findings**:
    - Franklin Attard and Jean-Pierre Ellul are associated with the highest negative inventory discrepancies (39 and 11 items missing, respectively). This may indicate a need for additional training or review of their inventory management practices.

### 4.4. Shift Distribution Analysis (Line_fig)

- **Purpose**: To understand shift-wise staff distribution.
- **Description**: A line chart showing the distribution of shifts (Morning, Afternoon, Evening) across different staff members.
- **Key Findings**:
    - The chart visualizes how shifts are distributed among staff, providing context for potential shift-related inventory issues.

### 4.5. Item Stock Discrepancy Analysis (df_stocks)

- **Purpose**: To identify items with the highest stock discrepancies.
- **Description**: Aggregated inventory discrepancy by Item ID and Category.
- **Key Findings**:
    - ITM002 (Yoga Mat) and ITM005 (Foam Roller) are the most frequently missing items, with 71 and 42 pieces missing, respectively. These are light items and might be prone to misplacement or theft.

### 4.6. Interactive Bar Chart (fig)

- **Purpose**: To allow interactive exploration of inventory discrepancies by different dimensions.
- **Description**: An interactive bar chart created using Panel and Plotly. Users can select different dimensions (Date, Month, Time, Responsible Staff, Category, Item ID, Weekday) using a radio button group to dynamically visualize inventory discrepancies.

### 4.7. KPI Cards (cards & stock discrepancy cards)

- **Purpose**: To highlight key performance indicators related to inventory management.
- **Description**: KPI cards are used to display:
    - The worst-performing day in terms of inventory discrepancy (KPI card: 'The worst-performing day').
    - The staff member with the biggest inventory losses (KPI card: 'Franklin Attard the biggest Loser').
    - The shift with the highest missing rate (KPI card: 'Morning shift had the hieghest missing rate').
    - Total missing items (KPI card: 'Missing Items').
    - Total overstocked items (KPI card: 'Overstocked Items').
- **Key Metrics**:
    - Total overstock: 42 items (0.044% of total stock).
    - Total missing items: 113 items (Yoga Mat: 71, Foam Roller: 42).
    - Highest missing items day: May 30th & August 3rd (-23 items).
    - Highest overstock day: July 25th (+31 items).
    - Staff with most missing items: Franklin Attard (-39 items).
    - Weekday with most missing items: Tuesday (-94 items).
    - Shift with most missing items: Morning Shift (-84 items).

### 4.8. Sidebar Insights (sidebar_card & insight cards)

- **Purpose**: To provide summary information and key insights in the dashboard sidebar.
- **Description**: Sidebar cards display:
    - Total records in the dataset (2000).
    - Date range of the data (01-01-2024 to 30-09-2024).
    - Key insights derived from the analysis, such as the need for better morning shift management, monitoring of light items, and improvement in the recording system to address overstocking.

## 5. Conclusion and Recommendations

The inventory analysis reveals several key areas for improvement:

- **Morning Shift Management**: The morning shift shows a higher rate of missing items. Focused management and potentially additional staff training during morning shifts could help reduce discrepancies.
- **Light Item Monitoring**: Yoga Mats and Foam Rollers are frequently missing. These items should be stored and monitored in more secure or closely watched areas to prevent loss.
- **Tuesday Inventory Process Review**: Tuesdays consistently show high missing item counts. A review of the inventory management process specifically on Tuesdays is recommended to identify and rectify the cause.
- **Staff Training for Franklin Attard and Jean-Pierre Ellul**: Given their higher association with missing items, targeted training on inventory management best practices may be beneficial.
- **Recording System Improvement**: The presence of both overstock and missing items suggests potential issues with the inventory recording system. Implementing a more robust and accurate system could help minimize discrepancies.

By addressing these areas, PeakFit Essentials can improve its inventory management, reduce losses from missing items, and optimize stock levels.

## 6. How to Use the Dashboard

The interactive dashboard, generated from `PeakFIt_analysis2.ipynb`, provides a user-friendly interface to explore the inventory data. To use the dashboard:

# PeakFit Inventory Analysis Documentation

## 1. Project Overview

This document provides professional documentation for the PeakFit Inventory Analysis project. The project aims to analyze inventory data from PeakFit Essentials, a fitness equipment and supplement store, to identify discrepancies, understand stock patterns, and provide actionable insights for inventory management. The analysis is performed using a Jupyter Notebook (`PeakFIt_analysis2.ipynb`) and generates an interactive dashboard for visualizing key inventory metrics.

## 2. Data Description

The data is sourced from an Excel file named `PeakFit Essentials.xlsx`, sheet 'Sheet1'. It contains inventory records from January 1, 2024, to September 30, 2024. The dataset includes the following key columns:

- **Date**: Date of the inventory record.
- **Time**: Shift time (Morning, Afternoon, Evening).
- **Item ID**: Unique identifier for each item (e.g., ITM001).
- **Category**: Category of the item (e.g., Strength Training Equipment).
- **Expected Quantity**: Expected stock quantity.
- **Actual Quantity**: Actual stock quantity after inventory count.
- **Inventory Discrepancy**: Calculated as `Actual Quantity - Expected Quantity`. This is the primary metric analyzed in this project.
- **Responsible Staff**: Staff member responsible for the inventory record.

The dataset covers 6 items across 3 categories, managed by 6 staff members over three shifts daily.

## 3. Data Cleaning and Processing

The data cleaning and processing steps performed in the Jupyter Notebook are as follows:

1. **Data Loading**: The data is read from the Excel file `PeakFit Essentials.xlsx` using pandas.
2. **Dropping Unnecessary Columns**: Columns like 'Expired Items', 'Returned Items', 'Items Out for Sales', 'Items Out for Quality Control', and 'Items Out for Events' are dropped as they are not relevant to the core inventory discrepancy analysis.
3. **Date Conversion**: The 'Date' column is converted to datetime format for time-series analysis.
4. **Calculating Inventory Discrepancy**: A new column 'Inventory Discrepancy' is calculated by subtracting 'Expected Quantity' from 'Actual Quantity'. The original 'Expected Quantity' and 'Actual Quantity' columns are then dropped.
5. **Month Extraction**: A 'Month' column is extracted from the 'Date' column to facilitate monthly analysis.
6. **Category Correction**: The 'Category' column is corrected to ensure consistency and accuracy. Items are re-categorized as follows:
    - ITM001, ITM003, ITM006 are assigned to 'CTG001' (Strength Training Equipment).
    - ITM004 is assigned to 'CTG003' (Supplements - Protein Powder).
    - ITM005 is assigned to 'CTG004' (Recovery Tools - Foam Rollers).

## 4. Analysis and Visualizations

The Jupyter Notebook generates several visualizations and KPIs to analyze the inventory data:

### 4.1. Calendar Heatmap (Heat_fig)

- **Purpose**: To visualize inventory discrepancies across days and months.
- **Description**: A heatmap is generated where days of the month are on the y-axis and months are on the x-axis. The color intensity represents the magnitude of inventory discrepancy for each day. Red indicates negative discrepancy (missing items), and blue indicates positive discrepancy (overstock).
- **Key Findings**:
    - July 25th shows a significant overstock of 31 items.
    - May 30th and August 3rd show the highest missing records, with approximately 23 items missing on each day.

### 4.2. Weekday Bar Chart (Bar_fig)

- **Purpose**: To analyze inventory discrepancies by weekday.
- **Description**: A bar chart showing the total inventory discrepancy for each day of the week.
- **Key Findings**:
    - Tuesdays consistently show the highest negative inventory discrepancy, with about 94 items missing in total over the analyzed period. This suggests potential issues with inventory management on Tuesdays.

### 4.3. Staff Performance Analysis (Bar2_fig)

- **Purpose**: To identify staff members with the most significant inventory discrepancies.
- **Description**: A bar chart showing the sum of inventory discrepancies attributed to each responsible staff member.
- **Key Findings**:
    - Franklin Attard and Jean-Pierre Ellul are associated with the highest negative inventory discrepancies (39 and 11 items missing, respectively). This may indicate a need for additional training or review of their inventory management practices.

### 4.4. Shift Distribution Analysis (Line_fig)

- **Purpose**: To understand shift-wise staff distribution.
- **Description**: A line chart showing the distribution of shifts (Morning, Afternoon, Evening) across different staff members.
- **Key Findings**:
    - The chart visualizes how shifts are distributed among staff, providing context for potential shift-related inventory issues.

### 4.5. Item Stock Discrepancy Analysis (df_stocks)

- **Purpose**: To identify items with the highest stock discrepancies.
- **Description**: Aggregated inventory discrepancy by Item ID and Category.
- **Key Findings**:
    - ITM002 (Yoga Mat) and ITM005 (Foam Roller) are the most frequently missing items, with 71 and 42 pieces missing, respectively. These are light items and might be prone to misplacement or theft.

### 4.6. Interactive Bar Chart (fig)

- **Purpose**: To allow interactive exploration of inventory discrepancies by different dimensions.
- **Description**: An interactive bar chart created using Panel and Plotly. Users can select different dimensions (Date, Month, Time, Responsible Staff, Category, Item ID, Weekday) using a radio button group to dynamically visualize inventory discrepancies.

### 4.7. KPI Cards (cards & stock discrepancy cards)

- **Purpose**: To highlight key performance indicators related to inventory management.
- **Description**: KPI cards are used to display:
    - The worst-performing day in terms of inventory discrepancy (KPI card: 'The worst-performing day').
    - The staff member with the biggest inventory losses (KPI card: 'Franklin Attard the biggest Loser').
    - The shift with the highest missing rate (KPI card: 'Morning shift had the hieghest missing rate').
    - Total missing items (KPI card: 'Missing Items').
    - Total overstocked items (KPI card: 'Overstocked Items').
- **Key Metrics**:
    - Total overstock: 42 items (0.044% of total stock).
    - Total missing items: 113 items (Yoga Mat: 71, Foam Roller: 42).
    - Highest missing items day: May 30th & August 3rd (-23 items).
    - Highest overstock day: July 25th (+31 items).
    - Staff with most missing items: Franklin Attard (-39 items).
    - Weekday with most missing items: Tuesday (-94 items).
    - Shift with most missing items: Morning Shift (-84 items).

### 4.8. Sidebar Insights (sidebar_card & insight cards)

- **Purpose**: To provide summary information and key insights in the dashboard sidebar.
- **Description**: Sidebar cards display:
    - Total records in the dataset (2000).
    - Date range of the data (01-01-2024 to 30-09-2024).
    - Key insights derived from the analysis, such as the need for better morning shift management, monitoring of light items, and improvement in the recording system to address overstocking.

## 5. Conclusion and Recommendations

The inventory analysis reveals several key areas for improvement:

- **Morning Shift Management**: The morning shift shows a higher rate of missing items. Focused management and potentially additional staff training during morning shifts could help reduce discrepancies.
- **Light Item Monitoring**: Yoga Mats and Foam Rollers are frequently missing. These items should be stored and monitored in more secure or closely watched areas to prevent loss.
- **Tuesday Inventory Process Review**: Tuesdays consistently show high missing item counts. A review of the inventory management process specifically on Tuesdays is recommended to identify and rectify the cause.
- **Staff Training for Franklin Attard and Jean-Pierre Ellul**: Given their higher association with missing items, targeted training on inventory management best practices may be beneficial.
- **Recording System Improvement**: The presence of both overstock and missing items suggests potential issues with the inventory recording system. Implementing a more robust and accurate system could help minimize discrepancies.

By addressing these areas, PeakFit Essentials can improve its inventory management, reduce losses from missing items, and optimize stock levels.


