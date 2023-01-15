# Write your MySQL query statement below
SELECT DISTINCT w1.id AS Id
FROM Weather AS w1, Weather AS w2
WHERE subdate(w1.recordDate,1) = w2.recordDate
AND w1.temperature > w2.temperature


# WHERE w1.temperature > (
#     SELECT temperature
#     FROM Weather AS w2
#     WHERE w1.recordDate = w2.recordDate + 1)