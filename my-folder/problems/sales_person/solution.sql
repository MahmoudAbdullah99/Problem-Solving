# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson AS s
LEFT JOIN (
    SELECT o.sales_id, o.order_id
    FROM Orders AS o
    INNER JOIN Company AS c 
    ON o.com_id = c.com_id
    WHERE c.name = 'RED') AS t
ON s.sales_id = t.sales_id
WHERE t.order_id IS NULL;