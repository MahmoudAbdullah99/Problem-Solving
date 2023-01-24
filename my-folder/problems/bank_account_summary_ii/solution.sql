# Write your MySQL query statement below
SELECT u.name, SUM(t.amount) AS balance 
FROM Users AS u
INNER JOIN Transactions AS t
USING(account)
GROUP BY u.account
HAVING SUM(t.amount) > 10000;