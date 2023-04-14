# Write your MySQL query statement below
SELECT
    e.name as Employee
FROM 
    Employee as e
    INNER JOIN
    Employee as e2
    ON e.managerId = e2.id
WHERE
    e2.salary < e.salary

