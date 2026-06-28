use retail_project;

select count(*) AS total_rows
from sales;

select *
from sales
limit 5;

select Description,
	sum(Revenue) AS total_revenue
from sales
group by Description 
order by total_revenue desc
limit 10;

select Customer_ID,
	sum(Revenue) AS total_spent
from sales
group by Customer_ID
order by total_spent desc
limit 10;

Select Country,
	sum(Revenue) as total_revenue
from sales
group by Country
order by total_revenue desc
limit 10;

select Country,
	count(distinct Invoice) as total_orders
From sales
group by Country
order by total_orders desc
limit 10;

select
	round(SUM(Revenue) / COUNT(DISTINCT InvoiceNo), 2) as avg_order_value
from sales;

select
	date_format(InvoiceDate, '%Y-%M') AS Month,
    round(SUM(Revenue), 2) as Monthly_Revenue
from sales
group by Month
order by Month;