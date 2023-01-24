# Write your MySQL query statement below
SELECT t.actor_id, t.director_id
FROM (
    SELECT actor_id, director_id, COUNT(timestamp) as count_cooperation
    FROM ActorDirector
    GROUP BY actor_id, director_id
) AS t
WHERE t.count_cooperation >= 3;