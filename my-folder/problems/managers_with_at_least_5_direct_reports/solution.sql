# Write your MySQL query statement below
SELECT
    e2.name
FROM 
    Employee e
    JOIN
    Employee e2
    ON e2.id = e.managerId
GROUP BY
    e.managerId
HAVING
    COUNT(e.managerId) >= 5
