# Write your MySQL query statement below
SELECT
    t.player_id,
    t.event_date AS first_login
FROM (
    SELECT
        player_id,
        event_date,
        RANK() OVER(
        PARTITION BY
            player_id
        ORDER BY
            event_date
    ) AS rnk
    FROM
        Activity
) AS t
WHERE t.rnk = 1;