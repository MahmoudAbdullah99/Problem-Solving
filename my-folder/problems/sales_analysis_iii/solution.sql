# Write your MySQL query statement below
Select DISTINCT
    s.product_id,
    p.product_name
From
    Sales AS s
Inner Join
    Product AS p
ON s.product_id = p.product_id
Where
    p.product_id Not In (
        Select Distinct
            product_id
        From
            Sales
        Where
            sale_date Not Between '2019-01-01' And '2019-03-31'
    )
;