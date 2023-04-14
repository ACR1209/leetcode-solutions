# Write your MySQL query statement below
SELECT
    customer_id,
    COUNT(*) as count_no_trans
FROM 
    Visits as v
    LEFT JOIN
    Transactions as t
    ON t.visit_id = v.visit_id
WHERE
    t.transaction_id IS NULL
GROUP BY
    customer_id
ORDER BY
    count_no_trans
    