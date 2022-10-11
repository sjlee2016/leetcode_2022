select c.name as Customers
FROM customers AS c 
LEFT JOIN orders AS o 
ON c.id = o.customerid
WHERE o.customerid is null;