import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv('../Data/cleaned_retail_data.csv')

# Show first rows
print(df.head())

# Top 10 products by revenue
top_products = (
    df.groupby('Description')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 products:")
print(top_products)

# Plot top products
top_products.plot(kind='bar')

plt.title('Top 10 Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Convert InvoiceData to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Month column
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# Monthly revenue analysis
monthly_revenue = (
    df.groupby('Month')['Revenue']
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)

# Plot monthly revenue
monthly_revenue.plot()

plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Top customers by revenue
top_customers = (
    df.groupby('Customer ID')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Customers:")
print(top_customers)

# Plot top customers
top_customers.plot(kind='bar')

plt.title('Top 10 Customers by Revenue')
plt.xlabel('Customer ID')
plt.ylabel('Revenue')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print(df.columns)