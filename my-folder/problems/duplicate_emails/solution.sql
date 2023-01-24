# Write your MySQL query statement below
SELECT DISTINCT p1.email AS Email
FROM Person AS p1, Person AS p2
WHERE p1.id != p2.id
AND p1.email = p2.email
;