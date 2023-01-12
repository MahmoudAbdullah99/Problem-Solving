# Write your MySQL query statement below
SELECT
    (SELECT DISTINCT salary
    FROM Employee as e
    ORDER BY e.salary DESC
    LIMIT 1 OFFSET 1) AS SecondHighestSalary
