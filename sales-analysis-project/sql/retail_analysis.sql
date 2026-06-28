Create database retail_project;

Use retail_project;

Create table sales ( 
InvoiceNo varchar(20),
StockCode varchar(20),
Description TEXT,
Quantity INT,
InvoiceDate datetime,
Price decimal(10,2),
Customer_ID float,
Country varchar(50),
Revenue decimal(10,2)
);
