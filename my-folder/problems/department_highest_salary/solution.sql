# Write your MySQL query statement below
WITH CompleteEmployee AS (SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    Department as d
    JOIN
    Employee as e
    ON e.departmentId  = d.id
),
MaxSalaryPerDepartment AS (
     
        SELECT 
            Department,
            MAX(salary) as Salary
        FROM 
            CompleteEmployee 
        GROUP BY 
            Department
        
)

SELECT 
    Department,
    Employee,
    Salary
FROM
    CompleteEmployee as ce
WHERE
    EXISTS (SELECT 
                * 
            FROM 
                MaxSalaryPerDepartment as ms 
            WHERE 
                ce.Department  = ms.Department 
                AND ce.Salary = ms.Salary 
            )