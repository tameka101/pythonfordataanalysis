# !/usr/binenv python3
"""
Created on Sun Apr 26 14:33:34 2026

@author: meka2

Questions to be answered:

- How many sales have they made with amounts more than 1000
- How many sales have theymakde that belong to the Category "Tops" and have a Quantiy of 3.
- The Total Sales by Category
- Averafe Amount by Category and Status
- Total Sales by Fulfilment and Shipment Type
"""


import pandas as pd

sales_data = pd.read_excel('sales_data.xlsx')

# =============================================================================
# Exploring the data
# =============================================================================
#get a summary of sales data
sales_data.info()
 # Can also check data types here
sales_data.describe()

#looking at columns
print(sales_data.columns)

#Having a look at the first few rows of data
print(sales_data.head())

#Check the data types of the columns
print(sales_data.dtypes)

# =============================================================================
# Cleaning the data
# =============================================================================

#Check for missing values in our sales data
print(sales_data.isnull().sum())

#drop any rows that ahs missing/nan values
sales_data_dropped = sales_data.dropna()

#drop rows with missing amounts based on amount column
sales_data_cleaned = sales_data.dropna(subset = ['Amount'])

#Check for missing values in our slaes data
print(sales_data_cleaned.isnull().sum())

# =============================================================================
# Slicing and Filtering Daya
# =============================================================================

#Select a subset of data based on the Category Column
category_data = sales_data[sales_data['Category'] == 'Top']
print(category_data)

#Select a subset of our data where the Amount > 1000
high_amount_data = sales_data[sales_data['Amount'] > 1000]
print(high_amount_data)

#Select a subset of data based on mutiple conditions
filtered_data = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] == 3)]

# =============================================================================
# Aggreating Data
# =============================================================================

#total sales by category
category_totals = sales_data.groupby('Category') ['Amount'].sum()
category_totals = sales_data.groupby('Category', as_index=False) ['Amount'].sum()
category_totals = category_totals.sort_values('Amount', ascending=False)

#Calculate the average Amount by Category and Fulfilment
fulfilment_averages = sales_data.groupby(['Category', 'Fulfilment'], as_index=False) ['Amount'].mean()
fulfilment_averages = fulfilment_averages.sort_values('Amount', ascending=False)

#Calculate the average Amount by Category and Status
status_averages = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean()
status_averages = status_averages.sort_values('Amount', ascending=False)

#Calculate total sales by shipment and fulfilment
total_sales_shipandfulfil = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_shipandfulfil = total_sales_shipandfulfil.sort_values('Amount', ascending=False)
total_sales_shipandfulfil.rename(columns ={'Courier Status' : 'Shipment'}, inplace = True)
# =============================================================================
# Exporting the Data
# =============================================================================

status_averages.to_excel('average_sales_by_category_and_status.xlsx', index=False)
total_sales_shipandfulfil.to_excel('total_sales_by_ship_and_fufil.xlsx', index=False)
































