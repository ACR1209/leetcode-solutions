# Write your MySQL query statement below
SELECT
    name,
    SUM(amount) as balance
FROM
    Users as u
    INNER JOIN
    Transactions as t
    ON t.account = u.account
GROUP BY
    name
HAVING
    balance > 10000