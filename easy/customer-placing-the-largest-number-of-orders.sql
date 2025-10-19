-- Write your PostgreSQL query statement below
select customer_number from Orders 
GROUP BY customer_number order by count(*) desc limit 1