# Write your MySQL query statement below
SELECT u.employee_id 
FROM (
    SELECT * FROM Employees as e1
    LEFT JOIN Salaries as s1
    USING(employee_id)
    UNION
    SELECT * FROM Salaries as s2
    LEFT JOIN Employees as e2
    USING(employee_id)) as u
WHERE u.name IS NULL
    OR u.salary IS NULL
ORDER BY u.employee_id;