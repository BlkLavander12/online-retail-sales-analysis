import pandas as pd

# This function loads the dataset
df = pd.read_excel(r"C:\Users\lawre\Documents\Python\sales-analysis-project\Data\Online-retail dataset\online_retail_II.xlsx")

# To view the first rows
print(df.head())

# Remove missing customer IDs
df = df.dropna(subset=['Customer ID'])

# Remove negative quantites
df = df[df['Quantity'] > 0]

# Remove negative prices
df = df[df['Price'] > 0]

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['Price']

# Convert date column
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df = df[
    [
        'Invoice',
        'StockCode',
        'Description',
        'Quantity',
        'InvoiceDate',
        'Price',
        'Customer ID',
        'Country',
        'Revenue'
    ]
]

# Save cleaned dataset
df.to_csv('../Data/cleaned_retail_data.csv', index=False)

print("Cleaning complete!")